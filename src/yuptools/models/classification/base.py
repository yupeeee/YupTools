from typing import Any, List, Optional, Tuple, Union

from collections import OrderedDict
import numpy as np
import torch
from torchvision import models

from .config import *
from .warnings import *

__all__ = [
    "ImageClassificationModel",
]


def load_not_in_pytorch_model(
        model_name: str,
        pretrained: bool = False,
        weights_dir: str = not_in_pytorch_weights_dir,
) -> torch.nn.Module:
    # assertions
    is_valid_not_in_pytorch_model(model_name)

    family = model_name.split("_")[0]

    # DeiT
    if family == "deit":
        from .nets import deit

        model = getattr(deit, model_name)(pretrained=pretrained)

    # MLP-Mixer
    elif family == "mixer":
        from .nets.mixer import MlpMixer, CONFIGS

        model = MlpMixer(config=CONFIGS[not_in_pytorch_models[model_name]])

        if pretrained:
            model.load_from(
                np.load(f"{weights_dir}/imagenet1k_{not_in_pytorch_models[model_name]}.npz")
            )

    # PoolFormer
    elif family == "poolformer":
        from .nets import poolformer

        model = getattr(poolformer, model_name)()

        if pretrained:
            state_dict = torch.load(f"{weights_dir}/{model_name}.pth.tar")
            model.load_state_dict(state_dict)

    # PVT
    elif family == "pvt":
        from .nets import pvt

        model = getattr(pvt, model_name)()

        if pretrained:
            state_dict = torch.load(f"{weights_dir}/{model_name}.pth")
            model.load_state_dict(state_dict)

    else:
        raise

    return model


class ImageClassificationModel:
    def __init__(
            self,
            name: str,
            pretrained: bool = False,
            weights: Optional[str] = default_weights,
            weights_dir: Optional[str] = None,
            mode: str = default_mode,
            use_cuda: bool = False,
    ) -> None:
        # assertions
        is_valid_mode(mode)

        self.name = name
        self.pretrained = pretrained
        self.weights = weights
        self.weights_dir = weights_dir
        self.mode = mode
        self.use_cuda = use_cuda
        self.machine = "cuda" if use_cuda else "cpu"

        self.model = self.load_model()

    def __call__(
            self,
            x: Any,
    ) -> Any:
        x = x.to(device=self.machine)

        return self.model(x).detach()

    def clean_name(
            self,
    ) -> str:
        # PyTorch models
        if self.name in models.list_models():
            return models.get_model_weights(self.name).__name__.split("_Weights")[0]

        # not in PyTorch models
        else:
            # assertions
            is_valid_not_in_pytorch_model(self.name)

            return not_in_pytorch_models[self.name]

    def load_model(
            self,
    ) -> torch.nn.Module:
        if self.name in models.list_models():
            model = getattr(models, self.name)

            if self.pretrained:
                from .weights import load_pytorch_model_weights

                weights = load_pytorch_model_weights(self.name, self.weights)
                model = model(weights=weights)

            else:
                model = model(weights=None)

        else:
            model = load_not_in_pytorch_model(
                model_name=self.name,
                pretrained=self.pretrained,
                weights_dir=self.weights_dir,
            )

        if self.mode is not None:
            model = getattr(model, self.mode)()

        model = model.to(self.machine)

        return model

    def load_state_dict(
            self,
            state_dict_path: str,
    ) -> None:
        state_dict = OrderedDict([
            (".".join(k.split(".")[1:]), v)
            if k.split(".")[0] == "module"
            else (k, v) for k, v in torch.load(state_dict_path).items()
        ])

        self.model.load_state_dict(state_dict)

    def merge_preprocess(
            self,
            preprocess: torch.nn.Module,
    ) -> None:
        self.model = torch.nn.Sequential(
            preprocess,
            self.model,
        )

    def predict(
            self,
            x: Any,
            batch_size: Optional[int] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        if batch_size is not None:
            batches = x.split(batch_size, dim=0)

            y = []

            for batch in batches:
                y.append(self.__call__(batch))

            y = torch.cat(y, dim=0)

        else:
            y = self.__call__(x)

        confs = torch.nn.Softmax(dim=-1)(y).to("cpu")
        preds = torch.argmax(confs, dim=-1)

        return preds, confs

    def get_layer_ids(
            self,
    ) -> List[str]:
        from ..xray import get_layer_ids

        return get_layer_ids(self.model)

    def get_layer(
            self,
            idx_or_id: Union[int, str],
    ) -> torch.nn.Module:
        from ..xray import get_layer

        if isinstance(idx_or_id, int):
            layer_ids = self.get_layer_ids()

            layer_id = layer_ids[idx_or_id]

        elif isinstance(idx_or_id, str):
            layer_id = idx_or_id

        else:
            raise ValueError(f"Invalid input for 'idx_or_id'.")

        return get_layer(self.model, layer_id)

    def get_layer_weights(
            self,
            idx_or_id: Union[int, str],
    ) -> Union[torch.Tensor, None]:
        layer = self.get_layer(idx_or_id)

        if "weight" in layer.state_dict().keys():
            return layer.state_dict()["weight"].detach().to("cpu")

        else:
            return None
