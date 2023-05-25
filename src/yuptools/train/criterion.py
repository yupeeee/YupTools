import torch
from torch import nn

__all__ = [
    "build_criterion",
]

criterions = [
    "CrossEntropyLoss",
]


def assertion(
        criterion_type: str,
) -> None:
    assert criterion_type in criterions, \
        f"Unsupported criterion type: {criterion_type}"


def build_criterion(
        config,
) -> torch.nn.Module:
    """
    in config.yaml:
    ⋮
    CRITERION:
      TYPE: str
    ⋮
    """
    criterion_type = config.CRITERION.TYPE

    assertion(criterion_type)

    if criterion_type == "CrossEntropyLoss":
        criterion = nn.CrossEntropyLoss()

    else:
        raise

    return criterion
