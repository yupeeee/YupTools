from typing import Any, Dict

import torch
from torch.utils.data import DataLoader
import tqdm

__all__ = [
    "CalibrationTest",
]


class CalibrationTest:
    def __init__(
            self,
            num_bins: int = 10,
            batch_size: int = 64,
            use_cuda: bool = False,
            verbose: bool = False,
    ) -> None:
        self.num_bins = num_bins
        self.batch_size = batch_size
        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"
        self.verbose = verbose

    def __call__(
            self,
            dataset,
            model: torch.nn.Module,
    ) -> Dict[str, Any]:
        dataloader = DataLoader(
            dataset=dataset,
            batch_size=self.batch_size,
        )

        signed_pred_confs = []

        for (data, targets) in tqdm.tqdm(
                dataloader,
                desc=f"Calibration Test",
                disable=not self.verbose,
        ):
            data, targets = data.to(self.machine), targets.to(self.machine)

            outputs = model(data)

            confs = torch.nn.Softmax(dim=-1)(outputs)
            preds = torch.argmax(confs, dim=-1)

            res = preds == targets
            signs = (res.float() - 0.5) * 2

            pred_confs = confs[..., preds].diag()

            signed_pred_confs.append((pred_confs * signs).detach().to("cpu"))

        signed_pred_confs = torch.cat(signed_pred_confs, dim=0)

        ece_data = self.ece(signed_pred_confs)

        return ece_data

    def ece(
            self,
            signed_pred_confs: torch.Tensor,
    ) -> Dict[str, Any]:
        num_data = len(signed_pred_confs)

        bins = torch.linspace(0, 1, self.num_bins + 1)

        bin_sizes = []
        mid_confs = []
        avg_confs = []
        accs = []

        for i in range(self.num_bins):
            min_conf = bins[i]
            max_conf = bins[i + 1]

            mid_conf = (min_conf + max_conf) / 2
            mid_confs.append(mid_conf)

            target_confs = [v for v in signed_pred_confs if min_conf < abs(v) <= max_conf]

            bin_size = len(target_confs)
            bin_sizes.append(bin_size)

            num_corrects = len([v for v in target_confs if v > 0])

            if num_corrects == 0:
                avg_confs.append(mid_conf)
                accs.append(0)
            else:
                avg_confs.append(sum([abs(v) for v in target_confs]) / bin_size)
                accs.append(num_corrects / bin_size)

        error = 0.
        signed_error = 0.

        for i in range(self.num_bins):
            bin_error = abs(accs[i] - avg_confs[i])
            signed_bin_error = accs[i] - avg_confs[i]

            error += bin_error * (bin_sizes[i] / num_data)
            signed_error += signed_bin_error * (bin_sizes[i] / num_data)

        return {
            "num_data": num_data,
            "bins": bins,
            "bin_sizes": bin_sizes,
            "mid_confs": mid_confs,
            "avg_confs": avg_confs,
            "accs": accs,
            "ECE": error,
            "sECE": signed_error,
        }
