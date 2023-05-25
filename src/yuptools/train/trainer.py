from typing import Optional

from .base import Trainer

__all__ = [
    "SupervisedLearner",
]


class SupervisedLearner(Trainer):
    def __init__(
            self,
            train_dataset,
            val_dataset,
            model,
            config_path: str,
            model_name: Optional[str],
            use_cuda: bool = False,
    ) -> None:
        super().__init__(
            train_dataset=train_dataset,
            val_dataset=val_dataset,
            model=model,
            config_path=config_path,
            model_name=model_name,
            use_cuda=use_cuda,
        )
