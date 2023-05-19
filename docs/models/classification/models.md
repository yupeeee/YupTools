# yuptools.models.classification.models

Classification models trained on specific datasets.


- [ImageNetClassificationModel](#imagenetclassificationmodel)


---


## ImageNetClassificationModel

Initializes an ImageNet classification model.

```
from yuptools.models import ImageNetClassificationModel

model = ImageNetClassificationModel(
    name: str,
    pretrained: bool = False,
    weights: str = None,
    weights_dir: str = None,
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

- **weights** (*str*):
Specifies which pretrained weights to use for models supported by PyTorch.
See ***Table of all available classification weights*** in [**link**](https://pytorch.org/vision/stable/models.html) for more details, and possible values.
Default is *"IMAGENET1K_V1"*.

- **weights_dir** (*str*):
Directory to search for the pretrained weights of models unsupported by PyTorch.
**Must be initialized if loading a model unsupported by PyTorch**.

- **mode** (*str*):
Mode of the model.
Must be one of *[None, "train", "eval", ]*.
Default is *None*.

- **use_cuda** (*bool*):
Specifies whether to use CUDA for GPU acceleration.
Default is *False*.
