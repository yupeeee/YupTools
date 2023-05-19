from typing import List

import torch

__all__ = [
    "get_params",
    "exponential_string_to_float",
    "reshape_classifier_output",
]


def get_params(
        module: torch.nn.Module,
) -> List[str]:
    attrs = ")".join(
        "(".join(
            str(module).replace(" ", "")
            .split("(")[1:])
        .split(")")[:-1]).split(",")

    params = []
    i = 0

    while i < len(attrs):
        if "(" in attrs[i] and ")" in attrs[i + 1]:
            params.append(f"{attrs[i]}, {attrs[i + 1]}")
            i += 1
        else:
            params.append(attrs[i])

        i += 1

    return params


def exponential_string_to_float(
        exponential: str,
) -> float:
    num, exponent = exponential.split("e")

    return float(f"{num}E{exponent}")


def replace_layer(
        self,
        model: torch.nn.Module,
        replacer,
        use_cuda: bool = False,
) -> None:
    for child_name, child in model.named_children():
        class_name = str(child.__class__).split(".")[-1].split("'")[0]

        if self.target == class_name:
            setattr(model, child_name, replacer(child, use_cuda))
        else:
            self.replace_layer(child, replacer)


def reshape_classifier_output(
        model,
        out_features: int,
        use_cuda: bool = False,
) -> None:
    child_name, child = list(model.named_children())[-1]

    class_name = str(child.__class__).split(".")[-1].split("'")[0]

    if class_name == "Linear":
        params = get_params(child)

        in_features = int(params[0].split("=")[-1])
        bias = bool(params[2].split("=")[-1])

        setattr(
            model,
            child_name,
            torch.nn.Linear(
                in_features=in_features,
                out_features=out_features,
                bias=bias,
                device="cuda" if use_cuda else "cpu",
            )
        )

    else:
        reshape_classifier_output(child, out_features)
