# yuptools.models.classification.models

Classification models trained on specific datasets.

- [CIFAR10ClassificationModel](#cifar10classificationmodel)
- [CIFAR100ClassificationModel](#cifar100classificationmodel)
- [ImageNetClassificationModel](#imagenetclassificationmodel)


---


## CIFAR10ClassificationModel

Initializes a CIFAR-10 classification model.

```
from yuptools.models import CIFAR10ClassificationModel

model = CIFAR10ClassificationModel(
    name: str,
    weights_path: str = None,
    mode: str = None,
    use_cuda: bool = False,
)
```

### Parameters

- **name** (*str*):
Name of the model.

- **weights_path** (*str*):
Path to the pretrained weights.
If specified, loads the pretrained weights to the model.
Default is *None*, i.e., *pretrained=False*.

- **mode** (*str*):
Mode of the model.
Must be one of *[None, "train", "eval", ]*.
Default is *None*.

- **use_cuda** (*bool*):
Specifies whether to use CUDA for GPU acceleration.
Default is *False*.


---


## CIFAR100ClassificationModel

Initializes a CIFAR-100 classification model.

```
from yuptools.models import CIFAR100ClassificationModel

model = CIFAR100ClassificationModel(
    name: str,
    weights_path: str = None,
    mode: str = None,
    use_cuda: bool = False,
)
```

### Parameters

- **name** (*str*):
Name of the model.

- **weights_path** (*str*):
Path to the pretrained weights.
If specified, loads the pretrained weights to the model.
Default is *None*, i.e., *pretrained=False*.

- **mode** (*str*):
Mode of the model.
Must be one of *[None, "train", "eval", ]*.
Default is *None*.

- **use_cuda** (*bool*):
Specifies whether to use CUDA for GPU acceleration.
Default is *False*.


---


## ImageNetClassificationModel

Initializes an ImageNet classification model.

```
from yuptools.models import ImageNetClassificationModel

model = ImageNetClassificationModel(
    name: str,
    pretrained: bool = False,
    weights: Optional[str] = default_weights,
    weights_dir: Optional[str] = None,
    mode: str = None,
    use_cuda: bool = False,
)
```

### Parameters

- **name** (*str*):
Name of the model.

- **pretrained** (*bool*):
Specifies whether to load pretrained weights for the model.
Default is *False*.

- **weights** (*str, optional*):
Specifies which pretrained weights to use for models supported by PyTorch.
See ***Table of all available classification weights*** in [**link**](https://pytorch.org/vision/stable/models.html) for more details, and possible values.
Default is *"IMAGENET1K_V1"*.

- **weights_dir** (*str, optional*):
Directory to search for the pretrained weights of models unsupported by PyTorch.
**Must be initialized if loading a model unsupported by PyTorch**.

- **mode** (*str*):
Mode of the model.
Must be one of *[None, "train", "eval", ]*.
Default is *None*.

- **use_cuda** (*bool*):
Specifies whether to use CUDA for GPU acceleration.
Default is *False*.
