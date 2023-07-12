from typing import Tuple, Union

import numpy as np
import torch
from torchvision import transforms as tf

__all__ = [
    "image_entropy",
]


def image_entropy(
        image: torch.Tensor,
        method: str = "gray",
        return_entropy_mat: bool = True,
) -> Union[float, Tuple[float, torch.Tensor]]:
    if len(image.shape) == 2:
        image = image.unsqueeze(dim=0)

    elif len(image.shape) == 3 and method == "gray":
        image = tf.Grayscale()(image)

    c, h, w = image.shape
    assert c in [1, 3, ]

    image = image.to(torch.float32)

    if method == "rgb":
        for i in range(c):
            image[i] = image[i] + torch.ones(size=(h, w)) * 255 * i

        image = torch.sum(image, dim=0)

    elif method == "gray":
        image = image[0]

    # grayscale image: 0 ~ 255
    if c == 1:
        bins = np.arange(256 + 1)

    # rgb image: 0 ~ 255*(1+2+3)
    elif c == 3:
        bins = np.arange(256 * 6 + 1)

    else:
        raise

    hist, _ = np.histogram(image.reshape(-1), bins=bins)
    probs = hist / (h * w)

    # entropy
    _probs = list(filter(lambda p: p > 0, np.ravel(probs)))  # probs wo/ zero
    entropy = -np.sum(np.multiply(_probs, np.log2(_probs)))

    if not return_entropy_mat:
        return entropy

    else:
        # entropy mat
        entropy_mat = torch.zeros_like(image)

        for i in range(h):
            for j in range(w):
                p = probs[int(image[i][j])]
                entropy_mat[i][j] = -p * np.log2(p)

        return entropy, entropy_mat
