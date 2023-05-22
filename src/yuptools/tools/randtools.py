import numpy as np
import random
import time
import torch

__all__ = [
    "set_random_seed",
    "unset_random_seed",
]


def set_random_seed(
        seed: int = None,
) -> None:
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)


def unset_random_seed() -> None:
    t = 1000 * time.time()  # current time in milliseconds
    seed = int(t) % 2 ** 32  # seed must be in range [0, 2^32-1]

    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
