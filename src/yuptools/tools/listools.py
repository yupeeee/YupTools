from typing import Any, List

__all__ = [
    "argmax_list",
    "argmin_list",
]


def argmax_list(
        lst: List[Any],
) -> int:
    return lst.index(max(lst))


def argmin_list(
        lst: List[Any],
) -> int:
    return lst.index(min(lst))
