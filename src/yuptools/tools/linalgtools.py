from typing import Union

import torch

__all__ = [
    "repeat_tensor",
    "normalize_v",
    "proj_v1_to_v2",
    "orthogonal_to_v",
]


def repeat_tensor(
        tensor: torch.Tensor,
        repeat: int,
        dim: int = 0,
) -> torch.Tensor:
    return torch.repeat_interleave(tensor[None, ...], repeat, dim=dim)


def normalize_v(
        v: torch.Tensor,
        p: Union[str, int] = "fro",
) -> torch.Tensor:
    assert len(v.shape) == 1

    return v / torch.norm(v, p)


def proj_v1_to_v2(
        v1: torch.Tensor,
        v2: torch.Tensor,
) -> torch.Tensor:
    assert len(v1.shape) == len(v2.shape) == 1

    v2_norm = torch.norm(v2)
    proj_norm = torch.dot(v1, v2) / v2_norm

    return v2 / v2_norm * proj_norm


def orthogonal_to_v(
        v: torch.Tensor,
        seed: int = None,
) -> torch.Tensor:
    from .randtools import set_random_seed, unset_random_seed

    assert len(v.shape) == 1

    set_random_seed(seed)

    rand_v = torch.randn_like(v)
    proj_v = proj_v1_to_v2(rand_v, v)

    unset_random_seed()

    return rand_v - proj_v
