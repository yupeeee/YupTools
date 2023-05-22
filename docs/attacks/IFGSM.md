# yuptools.attacks.ifgsm.IFGSM

Implementation of the [Iterative-FGSM (I-FGSM, a.k.a. BIM)](https://arxiv.org/abs/1607.02533).


- [Properties](#properties)
- Methods
  - [call](#call)
  - [gradients](#gradients)


---


```
IFGSM(
    model: torch.nn.Module,
    alpha: float,
    iteration: int,
    epsilon: float,
    targeted: bool = False,
    bound: bool = False,
    seed: int = None,
    use_cuda: bool = False,
    verbose: bool = False,
)
```

## Properties

- **model** (*torch.nn.Module*):
PyTorch model that will be attacked.

- **alpha** (*float*):
Magnitude of the perturbation applied at each iteration.
Controls the strength of the attack at each step.

- **iteration** (*int*):
Number of iterations to perform.

- **epsilon** (*float*):
Maximum allowable perturbation magnitude.
Controls the overall strength of the attack.

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

- **verbose** (*bool*):
If *True*, progress information about the attack iterations will be displayed.
By default, it is set to *False*.


## Methods


### *call*

Performs the I-FGSM attack on the input data.

```
from torchvision import transforms as tf

from yuptools.attacks import IFGSM
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

attack = IFGSM(
    model=model.model,
    alpha=0.05/50,
    iteration=50,
    epsilon=0.05,
    targeted=False,
    bound=True,
    seed=None,
    use_cuda=True,
    verbose=True,
)

data, target = dataset[0]
data = data.unsqueeze(dim=0)
target = torch.Tensor([target, ]).to(torch.int64)

# before attack
pred, conf = model.predict(data)

# apply attack
_data = attack(data, target)
>>> IFGSM(alpha=0.001, iteration=50, epsilon=0.05, targeted=False, bound=True, seed=None):
    100%|██████████| 50/50 [00:01<00:00, 36.70it/s]

# after attack
_pred, _conf = model.predict(_data)
```


### gradients

Returns a list of gradients obtained at each iteration of the attack.

```
attack = IFGSM(...)

grads: List[torch.Tensor] = attack.gradients(
    data: torch.Tensor,
    targets: torch.Tensor,
)
```
