import torch

from .config import *

__all__ = [
    "Replacer",
]


class Replacer:
    def __init__(
            self,
            target: str,
            to: str,
            use_cuda: bool = False,
    ) -> None:
        self.target = target
        self.to = to
        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"

    def __call__(
            self,
            model: torch.nn.Module,
    ):
        if (self.target, self.to) in activation_replacements:
            from . import activation as lib

        elif (self.target, self.to) in normalization_replacements:
            from . import normalization as lib

        else:
            raise ValueError

        replacer = getattr(lib, f"{self.target}_to_{self.to}")

        self.replace_layer(model, replacer)

        return model

    def replace_layer(
            self,
            model: torch.nn.Module,
            replacer,
    ) -> None:
        for child_name, child in model.named_children():
            class_name = str(child.__class__).split(".")[-1].split("'")[0]

            if self.target == class_name:
                setattr(model, child_name, replacer(child, self.use_cuda))
            else:
                self.replace_layer(child, replacer)
