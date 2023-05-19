from collections import OrderedDict
import math
import torch
from torchvision.ops import Permute

__all__ = [
    "BatchNorm2d_to_LayerNorm",
    "LayerNorm_to_BatchNorm2d",
]


def BatchNorm2d_to_LayerNorm(
        module: torch.nn.Module,
        use_cuda: bool = False,
) -> torch.nn.Module:
    from .common import get_params, exponential_string_to_float

    num_features, eps, _, affine, _ = get_params(module)

    normalized_shape = (int(num_features),)

    eps = exponential_string_to_float(eps.split("=")[-1])

    elementwise_affine = bool(affine.split("=")[-1])

    return torch.nn.Sequential(OrderedDict([
        ("pre-permute", Permute(dims=[0, 2, 3, 1])),
        ("norm", torch.nn.LayerNorm(
            normalized_shape=normalized_shape,
            eps=eps,
            elementwise_affine=elementwise_affine,
            device="cuda" if use_cuda else "cpu",
        )),
        ("post-permute", Permute(dims=[0, 3, 1, 2])),
    ]))


def LayerNorm_to_BatchNorm2d(
        module: torch.nn.Module,
        use_cuda: bool = False,
) -> torch.nn.Module:
    from .common import get_params, exponential_string_to_float

    normalized_shape, eps, elementwise_affine = get_params(module)

    num_features = normalized_shape.split("(")[-1].split(")")[0].split(",")
    num_features = math.prod([int(v) for v in num_features if v != " "])

    eps = exponential_string_to_float(eps.split("=")[-1])

    affine = bool(elementwise_affine.split("=")[-1])

    return torch.nn.Sequential(OrderedDict([
        ("pre-permute", Permute(dims=[0, 3, 1, 2])),
        ("norm", torch.nn.BatchNorm2d(
            num_features=num_features,
            eps=eps,
            affine=affine,
            device="cuda" if use_cuda else "cpu",
        )),
        ("post-permute", Permute(dims=[0, 2, 3, 1])),
    ]))
