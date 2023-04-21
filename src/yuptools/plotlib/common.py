from typing import Tuple

import torch

__all__ = [
    "chw_to_hwc",
    "best_figsize_for_subplots",
]


def chw_to_hwc(
        images: torch.Tensor,
) -> torch.Tensor:
    dim = len(images.shape)
    assert dim in [3, 4]

    # chw -> hwc
    if dim == 3:
        return images.permute(1, 2, 0)

    # nchw -> nhwc
    else:
        return images.permute(0, 2, 3, 1)


def best_figsize_for_subplots(
        num_figs: int,
        desired_hw_ratio: Tuple[int, int] = (1, 1),
) -> Tuple[int, int]:
    from ..tools.listools import argmin_list

    # find minimum height and width w/ desired hw ratio
    grow = 1

    while True:
        h, w = desired_hw_ratio
        h, w = h * grow, w * grow
        size = h * w

        if size < num_figs:
            grow += 1
            continue

        break

    # optimize
    best = (h, w)
    err = size - num_figs

    while err > 0:
        candidates = [best]
        errs = [err]

        h_reduced_err = (h - 1) * w - num_figs
        w_reduced_err = h * (w - 1) - num_figs

        if h_reduced_err >= 0:
            candidates.append((h - 1, w))
            errs.append(h_reduced_err)

        if w_reduced_err >= 0:
            candidates.append((h, w - 1))
            errs.append(w_reduced_err)

        min_idx = argmin_list(errs)

        best = candidates[min_idx]
        err = errs[min_idx]

        if best == best:
            break

    return best
