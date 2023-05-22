from typing import Optional

import torch

from .config import *
from .warnings import *

__all__ = [
    "DirectionGenerator",
]


def post_process(
        direction: torch.Tensor,
        perp: bool = False,
        normalize: str = default_normalize,
        seed: int = None,
) -> torch.Tensor:
    from ..tools.linalgtools import normalize_v, orthogonal_to_v

    # assertions
    is_valid_direction_normalize_method(normalize)

    shape = direction.shape
    direction = direction.reshape(-1)

    # perpendicular
    if perp:
        direction = orthogonal_to_v(
            v=direction,
            seed=seed,
        )

    # normalize
    if normalize is not None:
        # normalize == "unit"
        direction = normalize_v(
            v=direction,
            p="fro",
        )

        # normalize == "dim"
        if normalize == "dim":
            direction = direction * len(direction) ** 0.5

    direction = direction.reshape(shape)

    return direction


class DirectionGenerator:
    def __init__(
            self,
            model: Optional[torch.nn.Module] = None,
            method: str = default_method,
            perp: bool = False,
            normalize: str = default_normalize,
            seed: int = default_seed,
            use_cuda: bool = False,
    ) -> None:
        # assertions
        is_valid_direction_method(method)

        self.model = model
        self.method = method
        self.normalize = normalize
        self.perp = perp
        self.seed = seed
        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"

        DirectionGenerator.__name__ = \
            f"{self.method}(" \
            f"perp={self.perp}, " \
            f"normalize={self.normalize}, " \
            f"seed={self.seed}" \
            f")"

    def __call__(
            self,
            data: torch.Tensor,
            targets: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        assert data is not None

        if self.method == "fgsm":
            from ..attacks.fgsm import FGSM

            assert targets is not None and self.model is not None

            direction = FGSM(
                model=self.model,
                epsilon=0.,
                targeted=False,
                bound=False,
                seed=self.seed,
                use_cuda=self.use_cuda,
            ).gradient(
                data=data,
                targets=targets,
            )

        elif self.method == "fgsm_targeted":
            from ..attacks.fgsm import FGSM

            assert targets is not None and self.model is not None

            direction = FGSM(
                model=self.model,
                epsilon=0.,
                targeted=True,
                bound=False,
                seed=self.seed,
                use_cuda=self.use_cuda,
            ).gradient(
                data=data,
                targets=targets,
            )

        else:
            raise

        direction = post_process(
            direction=direction,
            perp=self.perp,
            normalize=self.normalize,
            seed=self.seed + 1 if isinstance(self.seed, int) else self.seed,
        )

        return direction
