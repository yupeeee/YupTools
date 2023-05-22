__all__ = [
    "is_valid_direction_method",
    "is_valid_direction_normalize_method",
]


def is_valid_direction_method(
        method: str,
) -> None:
    from .config import direction_generation_methods

    assert method in direction_generation_methods, \
        f"Unsupported method {method}.\n" \
        f"Supported methods: {direction_generation_methods}"


def is_valid_direction_normalize_method(
        method: str,
) -> None:
    from .config import direction_normalize_methods

    assert method in direction_normalize_methods, \
        f"Unsupported method {method}.\n" \
        f"Supported methods: {direction_normalize_methods}"
