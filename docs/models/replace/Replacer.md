# yuptools.models.replace.base.Replacer

Python class for replacing specific layers in a PyTorch model.


- [Properties](#properties)
- Methods
  - [call](#call)


---


```
Replacer(
    target: str,
    to: str,
    use_cuda: bool = False,
)
```

## Properties

- **target** (*str*):
Target layer type to be replaced.

- **to** (*str*):
Replacement layer type.

- **use_cuda** (*bool*):
Specifies whether to use CUDA for GPU acceleration.
Default is *False*.


## Methods


### *call*

Replaces the target layer(s) with the specified replacement layer in the provided PyTorch model.
Supported replacements are as follows:
- ReLU ⇄ GELU
- BatchNorm2d ⇄ LayerNorm

```
from yuptools.models import ImageNetClassificationModel, Replacer

model = ImageNetClassificationModel(
    name="resnet50",
    use_cuda=True,
    ...
)
print(model.get_layer(2))
>>> ReLU(inplace=True)

replacer = Replacer(
    target="ReLU",
    to="GELU",
    use_cuda=True,
)
model.model = replacer(model.model)
print(model.get_layer(2))
>>> GELU(approximate='none')
```
