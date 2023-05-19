from typing import Any

from torchvision import models

from .config import *
from .warnings import *

__all__ = [
    "load_pytorch_model_weights",
]


def load_pytorch_model_weights(
        model_name: str,
        weights: str = default_weights,
) -> models._api.WeightsEnum:
    # assertions
    is_valid_pytorch_model(model_name)
    is_valid_pytorch_model_weights(model_name, weights)

    return getattr(
        models.get_model_weights(model_name),
        weights,
    )


def download_not_in_pytorch_model_weights(
        model_name: str,
        save_dir: str = not_in_pytorch_weights_dir,
) -> Any:
    from ...tools.pathtools import mkdir

    pass  # TBD
