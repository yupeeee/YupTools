from typing import Callable, Dict, List

import torch

__all__ = [
    "get_layer_ids",
    "get_layer",

    "FeatureExtractor",
]


def is_attention_layer(
        layer_id: str,
) -> bool:
    # ViT
    if "self_attention" in layer_id:
        return True

    # Swin
    elif "attn" in layer_id:
        return True

    else:
        return False


def get_layer_ids(
        model: torch.nn.Module,
) -> List[str]:
    names = [name for name, _ in model.named_modules() if len(name)]

    layer_ids = []

    for i in range(len(names) - 1):
        if is_attention_layer(names[i]):
            layer_ids.append(names[i])
            continue

        if names[i] in names[i + 1]:
            continue

        else:
            layer_ids.append(names[i])

    layer_ids.append(names[-1])

    return layer_ids


def get_layer(
        model: torch.nn.Module,
        layer_id: str,
) -> torch.nn.Module:
    from ..tools.attrtools import get_attr

    return get_attr(model, layer_id)


class FeatureExtractor(torch.nn.Module):
    def __init__(
            self,
            model: torch.nn.Module,
            use_cuda: bool = False,
    ):
        super().__init__()

        self.model = model
        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"

        layer_ids = get_layer_ids(model)
        self.features = dict()

        self.hooks = []

        for layer_id in layer_ids:
            layer = get_layer(model, layer_id)
            layer_kind = layer.__class__.__name__

            self.hooks.append(
                layer.register_forward_hook(self.save_outputs_hook(layer_id, layer_kind))
            )

    def save_outputs_hook(
            self,
            layer_id: str,
            layer_kind: str,
    ) -> Callable:
        def fn(_, __, output):
            layer_key = f"{len(self.features)}-{layer_kind}-{layer_id}"

            if isinstance(output, tuple):
                output = [out for out in output if out is not None]
                output = torch.cat(output, dim=0)

            self.features[layer_key] = output.detach().cpu()

        return fn

    def forward(
            self,
            x: torch.Tensor,
    ) -> Dict[str, torch.Tensor]:
        _ = self.model(x.to(self.machine))

        for hook in self.hooks:
            hook.remove()

        return self.features
