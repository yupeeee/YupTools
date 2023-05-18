from typing import Any

__all__ = [
    "get_attr",
]


def get_attr(
        obj: Any,
        attrs: str,
) -> Any:
    for attr in attrs.split("."):
        try:
            obj = getattr(obj, attr)

        except AttributeError:
            raise

    return obj
