from typing import Optional

from .base import ImageClassificationModel
from .config import *


__all__ = [
    "ImageNetClassificationModel",
]


class ImageNetClassificationModel(ImageClassificationModel):
    def __init__(
            self,
            name: str,
            pretrained: bool = False,
            weights: Optional[str] = default_weights,
            weights_dir: Optional[str] = None,
            mode: str = default_mode,
            use_cuda: bool = False,
    ) -> None:
        super().__init__(
            name=name,
            pretrained=pretrained,
            weights=weights,
            weights_dir=weights_dir,
            mode=mode,
            use_cuda=use_cuda,
        )
