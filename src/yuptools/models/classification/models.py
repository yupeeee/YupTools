from typing import Optional

from .base import ImageClassificationModel
from .config import *

__all__ = [
    "CIFAR10ClassificationModel",
    "CIFAR100ClassificationModel",
    "ImageNetClassificationModel",
]


class CIFAR10ClassificationModel(ImageClassificationModel):
    def __init__(
            self,
            name: str,
            weights_path: str = None,
            mode: str = None,
            use_cuda: bool = False,
    ) -> None:
        from ..replace import reshape_classifier_output

        super().__init__(
            name=name,
            pretrained=False,
            weights=None,
            weights_dir=None,
            mode=mode,
            use_cuda=use_cuda,
        )

        reshape_classifier_output(
            model=self.model,
            out_features=10,
            use_cuda=use_cuda,
        )

        if weights_path is not None:
            self.load_state_dict(weights_path)


class CIFAR100ClassificationModel(ImageClassificationModel):
    def __init__(
            self,
            name: str,
            weights_path: str = None,
            mode: str = None,
            use_cuda: bool = False,
    ) -> None:
        from ..replace import reshape_classifier_output

        super().__init__(
            name=name,
            pretrained=False,
            weights=None,
            weights_dir=None,
            mode=mode,
            use_cuda=use_cuda,
        )

        reshape_classifier_output(
            model=self.model,
            out_features=100,
            use_cuda=use_cuda,
        )

        if weights_path is not None:
            self.load_state_dict(weights_path)


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
