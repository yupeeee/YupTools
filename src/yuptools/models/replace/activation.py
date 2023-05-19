import torch

__all__ = [
    "GELU_to_ReLU",
    "ReLU_to_GELU",
]


def GELU_to_ReLU(
        module: torch.nn.Module,
        use_cuda: bool = False,
) -> torch.nn.Module:
    return torch.nn.ReLU(
        inplace=True,
    )


def ReLU_to_GELU(
        module: torch.nn.Module,
        use_cuda: bool = False,
) -> torch.nn.Module:
    return torch.nn.GELU(
        approximate="none",
    )
