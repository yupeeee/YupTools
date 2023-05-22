# yuptools.attacks.fgsm.FGSM

Implementation of the [Fast Gradient Sign Method (FGSM)](https://arxiv.org/abs/1412.6572).


- [Properties](#properties)
- Methods
  - [call](#call)
  - [gradient](#gradient)


---


```
FGSM(
    model: torch.nn.Module,
    epsilon: float,
    targeted: bool = False,
    bound: bool = False,
    seed: int = None,
    use_cuda: bool = False,
)
```

## Properties

- **model** (*torch.nn.Module*):
PyTorch model that will be attacked.

- **epsilon** (*float*):
Magnitude of the perturbation.
Controls the strength of the attack.
Smaller values result in less noticeable perturbations.

- **targeted** (*bool*):
If *True*, the attack becomes a targeted attack,
where the goal is to manipulate the input to be classified as a specific target class.
By default, it is set to *False*.

- **bound** (*bool*):
If *True*, the values of the perturbed data are clipped to a valid range
(e.g., [0, 1] for image data).
By default, it is set to *False*.

- **seed** (*int*):
Seed for the random number generator used in the attack.
If *None*, the random seed is not set.
By default, it is set to *None*.

- **use_cuda** (*bool*):
If *True*, the attack will be performed on a CUDA-enabled GPU if available.
By default, it is set to *False*.


## Methods


### *call*

Performs the FGSM attack on the input data.

```
from torchvision import transforms as tf

from yuptools.attacks import FGSM
from yuptools.datasets import ImageNet, image_classification_transforms
from yuptools.models import ImageNetClassificationModel, default_weights

IMAGENET_DIR = ...

dataset = ImageNet(
    root=IMAGENET_DIR,
    split="val",
    transform=image_classification_transforms["centercrop256_resize224"],
    target_transform=None,
)

model = ImageNetClassificationModel(
    name="resnet50",
    pretrained=True,
    weights=default_weights,
    weights_dir=None,
    mode="eval",
    use_cuda=True,
)
model.merge_preprocess(
    preprocess=tf.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225],
    )
)

attack = FGSM(
    model=model.model,
    epsilon=0.05,
    targeted=False,
    bound=True,
    seed=None,
    use_cuda=True,
)

data, target = dataset[0]
data = data.unsqueeze(dim=0)
target = torch.Tensor([target, ]).to(torch.int64)

# before attack
pred, conf = model.predict(data)

# apply attack
_data = attack(data, target)

# after attack
_pred, _conf = model.predict(_data)
```


### gradient

Returns the adversarial gradient computed by FGSM.

```
attack = FGSM(...)

grad: torch.Tensor = attack.gradient(
    data: torch.Tensor,
    targets: torch.Tensor,
)
```
