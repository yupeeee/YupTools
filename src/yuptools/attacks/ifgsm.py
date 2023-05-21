from typing import List

import torch
import tqdm

__all__ = [
    "IFGSM",
]


class IFGSM:
    def __init__(
            self,
            model: torch.nn.Module,
            alpha: float,
            iteration: int,
            epsilon: float,
            targeted: bool = False,
            bound: bool = False,
            seed: int = None,
            use_cuda: bool = False,
            verbose: bool = False,
    ) -> None:
        self.model = model
        self.alpha = alpha
        self.iteration = iteration
        self.epsilon = epsilon
        self.targeted = targeted
        self.bound = bound
        self.seed = seed
        self.use_cuda = use_cuda
        self.machine = "cuda" if self.use_cuda else "cpu"
        self.verbose = verbose

        IFGSM.__name__ = \
            f"IFGSM(" \
            f"alpha={alpha}, " \
            f"iteration={iteration}, " \
            f"epsilon={epsilon}, " \
            f"targeted={targeted}, " \
            f"bound={bound}, " \
            f"seed={seed}" \
            f")"

    def __call__(
            self,
            data: torch.Tensor,
            targets: torch.Tensor,
    ) -> torch.Tensor:
        from .fgsm import FGSM

        fgsm = FGSM(
            model=self.model,
            epsilon=self.alpha,
            targeted=self.targeted,
            bound=self.bound,
            seed=self.seed,
            use_cuda=self.use_cuda,
        )

        _data = data.detach()

        for _ in tqdm.trange(
                self.iteration,
                desc=self.__class__.__name__,
                disable=not self.verbose,
        ):
            fgsm_grad = fgsm.gradient(_data, targets)
            pert = (fgsm_grad * self.alpha).clamp(-self.epsilon, self.epsilon)

            _data = data + pert

            if self.bound:
                _data = _data.clamp(0, 1)

        return _data

    def gradients(
            self,
            data: torch.Tensor,
            targets: torch.Tensor,
    ) -> List[torch.Tensor]:
        from .fgsm import FGSM

        fgsm = FGSM(
            model=self.model,
            epsilon=self.alpha,
            bound=self.bound,
            seed=self.seed,
            use_cuda=self.use_cuda,
        )

        _data = data.detach()
        grads = []

        for _ in tqdm.trange(
                self.iteration,
                desc=self.__class__.__name__,
                disable=not self.verbose,
        ):
            fgsm_grad = fgsm.gradient(_data, targets)
            grads.append(fgsm_grad)
            pert = (fgsm_grad * self.alpha).clamp(-self.epsilon, self.epsilon)

            _data = data + pert

            if self.bound:
                _data = _data.clamp(0, 1)

        return grads
