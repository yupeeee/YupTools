import torch

__all__ = [
    "FGSM",
]


class FGSM:
    def __init__(
            self,
            model: torch.nn.Module,
            epsilon: float,
            targeted: bool = False,
            bound: bool = False,
            seed: int = None,
            use_cuda: bool = False,
    ) -> None:
        self.model = model
        self.epsilon = epsilon
        self.targeted = targeted
        self.bound = bound
        self.seed = seed
        self.use_cuda = use_cuda
        self.machine = "cuda" if self.use_cuda else "cpu"

        FGSM.__name__ = \
            f"FGSM(" \
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
        grad = self.gradient(data, targets)
        pert = (grad * self.epsilon).clamp(-self.epsilon, self.epsilon)

        _data = data + pert

        if self.bound:
            _data = _data.clamp(0, 1)

        return _data

    def gradient(
            self,
            data: torch.Tensor,
            targets: torch.Tensor,
    ) -> torch.Tensor:
        from ..tools.randtools import set_random_seed

        set_random_seed(self.seed)

        data = data.detach().to(self.machine)
        targets = targets.detach().to(self.machine)

        data.requires_grad = True

        outputs = self.model(data)
        self.model.zero_grad()
        loss = torch.nn.CrossEntropyLoss()(outputs, targets)
        loss.backward()

        with torch.no_grad():
            data_grad = data.grad.data

        grad = data_grad.sign().detach().to("cpu")

        if self.targeted:
            grad = -grad

        return grad
