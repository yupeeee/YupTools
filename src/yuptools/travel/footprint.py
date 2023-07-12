from typing import Optional

import torch

from .config import *

__all__ = [
    "Footprint",
]


class Footprint:
    def __init__(
            self,
            step: int,
            model: torch.nn.Module,
            method: str = default_method,
            perp: bool = False,
            normalize: Optional[str] = default_normalize,
            bound: bool = False,
            seed: Optional[int] = default_seed,
            use_cuda: bool = False,
    ) -> None:
        from .direction import DirectionGenerator

        self.step = step
        self.model = model
        self.method = method
        self.perp = perp
        self.normalize = normalize
        self.bound = bound
        self.seed = seed
        self.use_cuda = use_cuda

        self.direction_generator = DirectionGenerator(
            model=model,
            method=method,
            perp=perp,
            normalize=normalize,
            seed=seed,
            use_cuda=use_cuda,
        )

        Footprint.__name__ = \
            f"{self.method}_footprint(" \
            f"step={self.step}, " \
            f"perp={self.perp}, " \
            f"normalize={self.normalize}, " \
            f"bound={self.bound}, " \
            f"seed={self.seed}" \
            f")"

    def __call__(
            self,
            data: torch.Tensor,
            epsilons: torch.Tensor,
            targets: Optional[torch.Tensor] = None,
            destinations: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        directions = self.direction_generator(
            data=data,
            targets=targets,
            destinations=destinations,
        )

        footprints = []

        for i in range(len(data)):
            footprints.append(
                self.generate_footprints(
                    data=data[i],
                    direction=directions[i],
                    epsilon=epsilons[i],
                ).unsqueeze(dim=0)
            )

        return torch.cat(footprints, dim=0)

    def generate_footprints(
            self,
            data: torch.Tensor,
            direction: torch.Tensor,
            epsilon: float,
    ) -> torch.Tensor:
        from ..tools.linalgtools import repeat_tensor

        footprints = repeat_tensor(
            tensor=data,
            repeat=self.step + 1,
            dim=0,
        )
        footprints_shape = footprints.shape

        if epsilon < 0:
            return torch.ones_like(footprints) * invalid_footprint_val

        directions = repeat_tensor(
            tensor=direction,
            repeat=self.step + 1,
            dim=0,
        ).reshape(self.step + 1, -1)

        strides = torch.linspace(0., epsilon, self.step + 1)

        footprints += (directions.T * strides).T.reshape(footprints_shape)

        if self.bound:
            footprints = footprints.clamp(0, 1)

        return footprints
