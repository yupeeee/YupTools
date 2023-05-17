from typing import List, Optional

import os
import shutil

__all__ = [
    "mkdir",
    "rmdir",
    "join_path",
    "ext",
    "ls",
]


def mkdir(
        path: str,
) -> None:
    os.makedirs(
        name=path,
        exist_ok=True,
    )


def rmdir(
        path: str,
) -> None:
    """WARNING: PERMANENT DELETION"""

    shutil.rmtree(path)


def join_path(
        path_list: List[str],
) -> str:
    return os.path.join(*path_list)


def ext(
        path: str,
) -> str:
    return os.path.splitext(path)[-1]


def ls(
        path: str,
        fext: Optional[str] = None,
        sort: bool = True,
) -> List[str]:
    file_list = os.listdir(path)

    if sort:
        from .listools import sort_str_list

        file_list = sort_str_list(
            str_list=file_list,
            return_indices=False,
        )

    if fext in [None, "", ]:
        return file_list

    # return directories (folders) only
    elif fext == "dir":
        return [
            f for f in file_list
            if os.path.isdir(os.path.join(path, f))
        ]

    # return files w/ specified extensions only
    else:
        return [
            f for f in file_list
            if ext(f) == "." + fext
        ]
