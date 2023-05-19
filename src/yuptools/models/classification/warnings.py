from torchvision import models

from .config import *

__all__ = [
    "is_valid_pytorch_model",
    "is_valid_pytorch_model_weights",
    "is_valid_not_in_pytorch_model",
    "is_valid_mode",
]


def is_valid_pytorch_model(
        model_name: str,
) -> None:
    assert model_name in models.list_models(), \
        f"PyTorch does not support model {model_name}."


def is_valid_pytorch_model_weights(
        model_name: str,
        weights: str,
) -> None:
    assert hasattr(models.get_model_weights(model_name), weights), \
        f"{model_name} has no weight {weights}."


def is_valid_not_in_pytorch_model(
        model_name: str,
) -> None:
    assert model_name in list(not_in_pytorch_models.keys()), \
        f"Unsupported model: {model_name}"


def is_valid_mode(
        mode: str,
) -> None:
    assert mode in modes, f"Unsupported mode: must be one of {modes}."
