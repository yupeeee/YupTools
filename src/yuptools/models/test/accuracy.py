import torch
from torch.utils.data import DataLoader
import tqdm

__all__ = [
    "AccuracyTest",
]


class AccuracyTest:
    def __init__(
            self,
            top_k: int = 1,
            batch_size: int = 64,
            use_cuda: bool = False,
            verbose: bool = False,
    ) -> None:
        self.top_k = top_k
        self.batch_size = batch_size
        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"
        self.verbose = verbose

    def __call__(
            self,
            dataset,
            model: torch.nn.Module,
    ) -> float:
        dataloader = DataLoader(
            dataset=dataset,
            batch_size=self.batch_size,
        )

        acc = 0.

        for (data, targets) in tqdm.tqdm(
                dataloader,
                desc=f"Accuracy Test",
                disable=not self.verbose,
        ):
            data, targets = data.to(self.machine), targets.to(self.machine)

            outputs = model(data)

            _, preds = outputs.topk(k=self.top_k, dim=-1)

            for k in range(self.top_k):
                acc += float(preds[:, k].eq(targets).sum().detach().to("cpu"))

        acc = acc / len(dataloader.dataset)

        return acc
