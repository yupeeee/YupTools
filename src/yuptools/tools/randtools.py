import numpy as np
import random
import torch

__all__ = [
    "set_random_seed",
]


def set_random_seed(
        seed: int = None,
) -> None:
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
