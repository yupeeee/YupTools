# yuptools.travel.travel.Traveler

Performs decision boundary travel in the input space
by iteratively adjusting the input data along the specified direction.
For further understanding of the idea of *travel* and *direction*,
refer to [**link**](https://arxiv.org/abs/2210.05742).


- [Properties](#properties)
- Methods
  - [call](#call)


---


```
Traveler(
    model: torch.nn.Module,
    method: str = default_method,
    perp: bool = False,
    normalize: str = default_normalize,
    bound: bool = False,
    seed: int = default_seed,
    use_cuda: bool = False,
    verbose: bool = False,
    init_eps: float = 1e-3,
    stride: float = 1e-3,
    stride_decay: float = 0.5,
    tol: float = 1e-10,
    max_iter: int = 10000,
    turnaround: float = 0.1,
)
```

## Properties

- **model** (*torch.nn.Module*):
PyTorch model for decision boundary travel.

- **method** (*str*):
Method for generating directions.
Available methods are listed below.
Default is *"fgsm"*.

    - **"fgsm"**: Generates direction using [FGSM](../attacks/FGSM.md).
    - **"fgsm_targeted"**: Generates direction using [FGSM (targeted=True)](../attacks/FGSM.md).
    - **"random"**: Generates an identical random direction for all input data.
    - **"random_signed"**: Generates an identical random direction for all input data,
        where each element can only be -1 or 1.

- **perp** (*bool*):
Determines if the generated directions should be perpendicular to the original direction.
Default is *False*.

- **normalize** (*str*):
Specifies the method to normalize directions.
Available methods are listed below.
Default is *"dim"*.

    - **"dim"**: Normalizes the direction $\mathrm{\mathbf{d}}$ as 
        $\|\mathrm{\mathbf{d}}\|_{2} = \sqrt{D}$,
        where $D$ is the dimension of $\mathrm{\mathbf{d}}$.
    - **"unit"**: Normalizes the direction $\mathrm{\mathbf{d}}$ as 
        $\|\mathrm{\mathbf{d}}\|_{2} = 1$.

- **bound** (*bool*):
Determines if the traveled data points should be bound within a specific range,
i.e., [0, 1] for image data.
Default is *False*.

- **seed** (*int*):
Random seed for direction generation.
Default is *None*.

- **use_cuda** (*bool*):
Determines if CUDA should be used for direction generation.
Default is *False*.

- **verbose** (*bool*):
Determines if progress information should be displayed.
Default is *False*.

- **init_eps** (*float*):
Initial epsilon value for travel.
Default is *1e-3*.

- **stride** (*float*):
The stride value for travel.
**Must be over 0**.
Default is *1e-3*.

- **stride_decay** (*float*):
The decay rate of the stride value after each travel iteration.
**Must have a value in range (0, 1)**.
Default is *0.5*.

- **tol** (*float*):
The tolerance value for considering convergence.
Default is *1e-10*.

- **max_iter** (*int*):
The maximum number of iterations for traveling.
Default is *10000*.

- **turnaround** (*float*):
The percentage of maximum iterations to wait before considering divergence.
Default is *0.1* (10%).


## Methods


### *call*

Generates traveled data points and their corresponding epsilon values
based on the specified method and input data (and targets). \
**Note**: Negative epsilon values (default: *-1.*) indicate either
the original misclassification of the corresponding data
or the failure of the travel process to converge.

- **data** (*torch.Tensor*):
Input data to be traveled.
It should be a tensor of shape (*batch_size*, ...),
where ... represents the shape of each data sample.

- **targets** (*torch.Tensor*):
Target of the input data.
It should be a 1-dimensional tensor of shape (*batch_size*, ).

```
from torchvision import transforms as tf

from src.yuptools.datasets import ImageNet, image_classification_transforms
from src.yuptools.models import ImageNetClassificationModel, default_weights
from src.yuptools.travel import Traveler

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

traveler = Traveler(
    model=model.model,
    method="fgsm",
    perp=False,
    normalize="dim",
    seed=0,
    bound=True,
    use_cuda=True,
    verbose=True,
)

data, targets = dataset.data_and_targets_of_class_c(c=0)
traveled_data, epsilons = traveler(data, targets)

print(traveled_data.shape)
print(epsilons.shape)

>>> [2/50] fgsm_travel(perp=False, normalize=dim, bound=True, seed=0):
    1%|          | 73/10000 [00:00<01:44, 95.43it/s]
    [4/50] fgsm_travel(perp=False, normalize=dim, bound=True, seed=0):
    1%|▏         | 138/10000 [00:01<01:42, 96.02it/s]
    [5/50] fgsm_travel(perp=False, normalize=dim, bound=True, seed=0):
    1%|          | 87/10000 [00:00<01:47, 92.02it/s]
    ...
    [50/50] fgsm_travel(perp=False, normalize=dim, bound=True, seed=0):
    1%|          | 75/10000 [00:00<01:44, 94.71it/s]
    torch.Size([50, 3, 224, 224])
    torch.Size([50])
```
