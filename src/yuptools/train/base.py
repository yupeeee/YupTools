from typing import Optional

from datetime import datetime
import time
import torch
import tqdm
import yaml

from ..tools import AttrDict

__all__ = [
    "Trainer",
]


def load_config(
        config_path: str,
) -> AttrDict:
    from ..tools.dictools import make_attrdict

    with open(config_path, "r") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    return make_attrdict(config)


class Trainer:
    def __init__(
            self,
            train_dataset,
            val_dataset,
            model: torch.nn.Module,
            config_path: str,
            model_name: Optional[str] = None,
            use_cuda: bool = False,
    ) -> None:
        from .criterion import build_criterion
        from .dataloader import build_dataloader
        from .scheduler import build_scheduler
        from .optimizer import build_optimizer

        self.model = model

        if model_name is None:
            model_name = self.model.__class__.__name__

        if hasattr(self.model, "name"):
            model_name = self.model.name

        self.model_name = model_name

        self.config = load_config(config_path)

        self.start_epoch = 1
        self.epochs = self.config.EPOCH

        self.train_dataloader = \
            build_dataloader(train_dataset, self.config)
        self.val_dataloader = \
            build_dataloader(val_dataset, self.config) \
                if val_dataset is not None else None

        self.criterion = build_criterion(self.config)

        self.optimizer = build_optimizer(model.model, self.config)

        self.scheduler = build_scheduler(self.optimizer, self.config, self.start_epoch)

        self.use_cuda = use_cuda

        self.datetime = datetime.now().strftime("%y%m%d%H%M%S")

        self.train_ID = \
            f"{self.train_dataloader.dataset.__class__.__name__}/" \
            f"{self.model_name}-{self.datetime}"

    def run(
            self,
            weights_save_root: str,
            log_save_root: str,
            weights_save_period: int = 1,
    ) -> None:
        from ..tools.dictools import load_csv_dict, save_dict_in_csv
        from ..tools.pathtools import mkdir, join_path

        best_eval_acc = 0.

        log_save_dir = join_path([
            log_save_root,
            self.train_ID,
        ])

        weights_save_dir = join_path([
            weights_save_root,
            self.train_ID,
        ])

        if self.start_epoch == 1:
            mkdir(log_save_dir)
            mkdir(weights_save_dir)

            # save train configuration
            with open(join_path([
                log_save_dir,
                "config.yaml",
            ]), "w") as f:
                yaml.dump(self.config, f, default_flow_style=False)

            # save initial model
            print(f"Saving initial weights to {weights_save_dir}...\n")
            torch.save(
                self.model.state_dict(),
                join_path([
                    weights_save_dir,
                    f"{self.model_name}-init.pth",
                ])
            )

            log = {
                "epoch": [],
                "lr": [],

                "train_time": [],
                "train_loss": [],
                "train_acc": [],
            }

            if self.val_dataloader is not None:
                log["eval_time"] = []
                log["eval_loss"] = []
                log["eval_acc"] = []

        else:
            log = load_csv_dict(
                csv_path=join_path([
                    log_save_dir,
                    "log.csv",
                ]),
                index_col=None,
            )

        for epoch in range(self.start_epoch, self.epochs + 1):
            # train
            lr, train_time, train_loss, train_acc = \
                self.train(epoch, self.model, self.train_dataloader)

            log["epoch"].append(epoch)
            log["lr"].append(lr)

            log["train_time"].append(train_time)
            log["train_loss"].append(train_loss)
            log["train_acc"].append(train_acc)

            self.scheduler.step()

            # eval
            if self.val_dataloader is not None:
                eval_time, eval_loss, eval_acc = \
                    self.eval(epoch, self.model, self.val_dataloader)

                log["eval_time"].append(eval_time)
                log["eval_loss"].append(eval_loss)
                log["eval_acc"].append(eval_acc)

            else:
                eval_acc = train_acc

            # save best model weights
            if eval_acc > best_eval_acc:
                best_eval_acc = eval_acc

                print(f"Saving best weights to {weights_save_dir}... (Epoch: {epoch})\n")
                torch.save(
                    self.model.state_dict(),
                    join_path([
                        weights_save_dir,
                        f"{self.model_name}-best.pth",
                    ])
                )

            # save model weights per weights_save_period
            if not epoch % weights_save_period:
                print(f"Saving weights to {weights_save_dir}...\n")
                torch.save(
                    self.model.state_dict(),
                    join_path([
                        weights_save_dir,
                        f"{self.model_name}-epoch_{epoch}.pth",
                    ])
                )

            # save train log
            save_dict_in_csv(
                dictionary=log,
                save_dir=log_save_dir,
                save_name="log",
                index_col="epoch",
            )

            # save checkpoint
            torch.save(
                {
                    "epoch": epoch,
                    "state_dict": self.model.state_dict(),
                    "optimizer": self.optimizer.state_dict(),
                },
                join_path([
                    log_save_dir,
                    "checkpoint.pt",
                ]),
            )

    def train(
            self,
            epoch: int,
            model: torch.nn.Module,
            dataloader: torch.utils.data.DataLoader,
    ):
        start = time.time()

        model.train()

        train_loss = 0.0
        train_acc = 0.0

        lr = self.optimizer.param_groups[0]["lr"]

        for (data, targets) in tqdm.tqdm(
                dataloader,
                desc=f"[EPOCH {epoch}/{self.epochs}] TRAIN (LR: {lr:0.8f})",
        ):
            if self.use_cuda:
                data, targets = data.to("cuda"), targets.to("cuda")

            self.optimizer.zero_grad()

            outputs = model(data)

            loss = self.criterion(outputs, targets)
            loss.requires_grad_(True)
            loss.backward()

            self.optimizer.step()

            train_loss += loss.item()

            _, preds = outputs.max(1)
            train_acc += float(preds.eq(targets).sum().detach().to("cpu"))

        finish = time.time()

        train_loss = train_loss / len(dataloader)
        train_acc = train_acc / len(dataloader.dataset)

        print(f"TRAIN LOSS: {train_loss:.8f}\tTRAIN ACC: {(train_acc * 100):.4f}%\n")

        return self.optimizer.param_groups[0]["lr"], finish - start, train_loss, train_acc

    @torch.no_grad()
    def eval(
            self,
            epoch: int,
            model: torch.nn.Module,
            dataloader: torch.utils.data.DataLoader,
    ):
        start = time.time()

        model.eval()

        eval_loss = 0.0
        eval_acc = 0.0

        for (data, targets) in tqdm.tqdm(
                dataloader,
                desc=f"[EPOCH {epoch}/{self.epochs}] EVAL",
        ):
            if self.use_cuda:
                data, targets = data.to("cuda"), targets.to("cuda")

            outputs = model(data)

            loss = self.criterion(outputs, targets)
            eval_loss += loss.item()

            _, preds = outputs.max(1)
            eval_acc += float(preds.eq(targets).sum().detach().to("cpu"))

        finish = time.time()

        eval_loss = eval_loss / len(dataloader)
        eval_acc = eval_acc / len(dataloader.dataset)

        print(f"EVAL LOSS: {eval_loss:.8f}\tEVAL ACC: {(eval_acc * 100):.4f}%\n")

        return finish - start, eval_loss, eval_acc

    def resume(
            self,
            weights_save_root: str,
            log_save_root: str,
            prev_datetime: str,
            weights_save_period: int = 1,
    ) -> None:
        from ..tools.pathtools import join_path
        from .scheduler import build_scheduler

        print(
            f"Resuming {prev_datetime}... "
            f"(dataset: {self.train_dataloader.dataset.__class__.__name__} / "
            f"model: {self.model_name})"
        )
        self.datetime = prev_datetime

        log_save_dir = join_path([
            log_save_root,
            self.train_ID,
        ])

        checkpoint = torch.load(join_path([
            log_save_dir,
            "checkpoint.pt",
        ]))

        stopped_epoch = checkpoint["epoch"]
        self.model.load_state_dict(checkpoint["state_dict"])
        self.optimizer.load_state_dict(checkpoint["optimizer"])

        self.start_epoch = stopped_epoch + 1

        self.scheduler = build_scheduler(self.optimizer, self.config, self.start_epoch)

        self.run(
            weights_save_root,
            log_save_root,
            weights_save_period,
        )
