from typing import Optional

from torchvision import transforms as tf

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

    def add_normalize_in_front(
            self,
    ) -> None:
        self.merge_preprocess(
            preprocess=tf.Normalize(
                mean=[0.4942, 0.4851, 0.4504],
                std=[0.2467, 0.2429, 0.2616],
            )
        )


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

    def add_normalize_in_front(
            self,
    ) -> None:
        self.merge_preprocess(
            preprocess=tf.Normalize(
                mean=[0.5071, 0.4865, 0.4409],
                std=[0.2673, 0.2564, 0.2762],
            )
        )


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

    def add_normalize_in_front(
            self,
    ) -> None:
        self.merge_preprocess(
            preprocess=tf.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225],
            )
        )
