__all__ = [
    "direction_generation_methods",
    "direction_normalize_methods",

    "default_method",
    "default_normalize",
    "default_seed",

    "eps_for_incorrect",
    "eps_for_divergence",
    "invalid_footprint_val",
]

direction_generation_methods = [
    "fgsm",
    "fgsm_targeted",
    "random",
    "random_signed",
]

direction_normalize_methods = [
    "dim",
    "unit",
]

default_method = "fgsm"
default_normalize = "dim"
default_seed = None

# invalids: must be negative
eps_for_incorrect = -1.
eps_for_divergence = -1.
invalid_footprint_val = -1.
