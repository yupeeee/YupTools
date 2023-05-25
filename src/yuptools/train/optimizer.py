import torch
from torch import optim
from torch.optim import Optimizer

__all__ = [
    "build_optimizer",
]

optimizers = [
    # "Adadelta",
    # "Adagrad",
    "Adam",
    "AdamW",
    # "SparseAdam",
    # "Adamax",
    # "ASGD",
    # "LBFGS",
    # "NAdam",
    # "RAdam",
    # "RMSprop",
    # "Rprop",
    "SGD",
]


def assertion(
        optimizer_type: str,
) -> None:
    assert optimizer_type in optimizers, \
        f"Unsupported optimizer type: {optimizer_type}"


def build_optimizer(
        model: torch.nn.Module,
        config,
) -> Optimizer:
    optimizer_type = config.OPTIMIZER.TYPE

    assertion(optimizer_type)

    if optimizer_type == "Adam":
        optimizer = Adam(model, config)

    elif optimizer_type == "AdamW":
        optimizer = AdamW(model, config)

    elif optimizer_type == "SGD":
        optimizer = SGD(model, config)

    else:
        raise

    return optimizer


def Adam(
        model: torch.nn.Module,
        config,
) -> Optimizer:
    """
    in config.yaml:
    ⋮
    LR: float
    ⋮
    OPTIMIZER:
      TYPE: Adam
      WEIGHT_DECAY: float
    ⋮
    """
    return optim.Adam(
        model.parameters(),
        lr=config.LR,
        betas=(0.9, 0.999),
        eps=1e-08,
        weight_decay=config.OPTIMIZER.WEIGHT_DECAY,
        amsgrad=False,
    )


def AdamW(
        model: torch.nn.Module,
        config,
) -> Optimizer:
    """
    in config.yaml:
    ⋮
    LR: float
    ⋮
    OPTIMIZER:
      TYPE: AdamW
      WEIGHT_DECAY: float
    ⋮
    """
    return optim.AdamW(
        params=model.parameters(),
        lr=config.LR,
        betas=(0.9, 0.999),
        eps=1e-08,
        weight_decay=config.OPTIMIZER.WEIGHT_DECAY,
        amsgrad=False,
    )


def SGD(
        model: torch.nn.Module,
        config,
) -> Optimizer:
    """
    in config.yaml:
    ⋮
    LR: float
    ⋮
    OPTIMIZER:
      TYPE: SGD
      MOMENTUM: float
      WEIGHT_DECAY: float
    ⋮
    """
    return optim.SGD(
        params=model.parameters(),
        lr=config.LR,
        momentum=config.OPTIMIZER.MOMENTUM,
        dampening=0,
        weight_decay=config.OPTIMIZER.WEIGHT_DECAY,
        nesterov=False,
    )
