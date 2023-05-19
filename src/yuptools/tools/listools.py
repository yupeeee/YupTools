from typing import Any, Dict, List, Tuple, Union

import re

__all__ = [
    "argmax_list",
    "argmin_list",
    "sort_str_list",
    "merge_list_of_lists",
    "merge_lists_in_dict",
]


def argmax_list(
        lst: List[Any],
) -> int:
    return lst.index(max(lst))


def argmin_list(
        lst: List[Any],
) -> int:
    return lst.index(min(lst))


def sort_str_list(
        str_list: List[str],
        return_indices: bool = False,
) -> Union[
    List[str],  # return_indices = False
    Tuple[List[str], List[int]],  # return_indices = True
]:
    convert = lambda text: int(text) if text.isdigit() else text

    sorted_str_list = sorted(
        str_list,
        key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)],
    )

    if not return_indices:
        return sorted_str_list

    else:
        indices = sorted(
            range(len(str_list)),
            key=lambda key: [convert(c) for c in re.split('([0-9]+)', str_list[key])],
        )

        return sorted_str_list, indices


def merge_list_of_lists(
        list_of_lists: List[List[Any]],
) -> List[Any]:
    return [item for sublist in list_of_lists for item in sublist]


def merge_lists_in_dict(
        dictionary: Dict[Any, List[Any]],
) -> List[Any]:
    lst = []

    for key in dictionary:
        value: List = dictionary[key]

        lst.append(value)

    lst = merge_list_of_lists(lst)

    return lst
