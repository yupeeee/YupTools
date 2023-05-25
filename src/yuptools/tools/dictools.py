from typing import Any, Dict, List

import pandas as pd

__all__ = [
    "load_csv_dict",
    "dict_to_df",
    "save_dict_in_csv",
    "AttrDict",
    "make_attrdict",
]


def load_csv_dict(
        csv_path: str,
        index_col: Any = 0,
) -> Dict[Any, List[Any]]:
    df = pd.read_csv(csv_path, index_col=index_col)

    return df.to_dict(orient="list")


def dict_to_df(
        dictionary: Dict,
        index_col: Any = None,
) -> pd.DataFrame:
    df = pd.DataFrame(dictionary)

    if index_col is not None:
        df.set_index(index_col)

    return df


def save_dict_in_csv(
        dictionary: Dict,
        save_dir: str,
        save_name: str,
        index_col: Any = None,
) -> None:
    from .pathtools import mkdir, join_path

    mkdir(save_dir)

    save_path = join_path([
        save_dir,
        f"{save_name}.csv",
    ])

    df = dict_to_df(dictionary, index_col)

    if index_col is not None:
        df.to_csv(save_path, mode="w", index=False)

    else:
        df.to_csv(save_path, mode="w")


class AttrDict(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError(f"No such attribute: {name}")

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError(f"No such attribute: {name}")


def make_attrdict(
        dictionary: Dict,
) -> AttrDict:
    dictionary = AttrDict(dictionary)

    for key, value in dictionary.items():
        if isinstance(value, dict):
            dictionary[key] = make_attrdict(value)

    return dictionary


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
