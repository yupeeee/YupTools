# yuptools.datasets.image_classification

Common datasets and transforms used in image classification tasks.


- [image_classification_transforms](#image_classification_transforms)
<br/><br/>
- [Caltech101](#caltech101)
- [Caltech256](#caltech256)
- [CIFAR10](#cifar10)
- [CIFAR100](#cifar100)
- [Country211](#country211)
- [FashionMNIST](#fashionmnist)
- [ImageNet](#imagenet)
- [MNIST](#mnist)


---


## image_classification_transforms

Common transforms used in image classification tasks.
Type is *Dict[str, TRANSFORM]*.
The transforms transform *Union[PIL.Image, numpy.ndarray]* to *torch.Tensor*.

```
from yupeeee_pytools.datasets import image_classification_transforms as transforms

transform = transforms["default"]
```

### Keys (Transform types)

- **default**:
Convert a PIL Image or ndarray to tensor and scale the values accordingly.

- **resize28**:
  1) Resize the given PIL Image or ndarray to a 28*28 square size.
  2) Convert the resized image to tensor and scale the values accordingly.

- **resize32**:
  1) Resize the given PIL Image or ndarray to a 32*32 square size.
  2) Convert the resized image to tensor and scale the values accordingly.

- **resize224**:
  1) Resize the given PIL Image or ndarray to a 224*224 square size.
  2) Convert the resized image to tensor and scale the values accordingly.

- **resize256**:
  1) Resize the given PIL Image or ndarray to a 256*256 square size.
  2) Convert the resized image to tensor and scale the values accordingly.

- **centercrop256_resize224**:
  1) Crop the given PIL Image or ndarray at the center to a 256*256 square size.
  2) Resize the cropped image to a 224*224 square size.
  3) Convert the resized image to tensor and scale the values accordingly.


---


## Caltech101

[Caltech 101](https://data.caltech.edu/records/mzrjq-6wc02) dataset.

```
from yupeeee_pytools.datasets import Caltech101

dataset = Caltech101(
    root: str,
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.


---


## Caltech256

[Caltech 256](https://data.caltech.edu/records/nyy15-4j048) dataset.

```
from yupeeee_pytools.datasets import Caltech256

dataset = Caltech256(
    root: str,
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.


---


## CIFAR10

[CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset.

```
from yupeeee_pytools.datasets import CIFAR10

dataset = CIFAR10(
    root: str,
    train: bool = True,
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **train** (*bool, optional*):
If *True*, creates dataset from training set, otherwise creates from test set.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.


---


## CIFAR100

[CIFAR-100](https://www.cs.toronto.edu/~kriz/cifar.html) dataset.

```
from yupeeee_pytools.datasets import CIFAR100

dataset = CIFAR100(
    root: str,
    train: bool = True,
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **train** (*bool, optional*):
If *True*, creates dataset from training set, otherwise creates from test set.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.


---


## Country211

[The Country211 Dataset](https://github.com/openai/CLIP/blob/main/data/country211.md) from OpenAI.

```
from yupeeee_pytools.datasets import Country211

dataset = Country211(
    root: str,
    split: str = "train",
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **split** (*string, optional*):
The dataset split; supports *"train"* (default), *"valid"*, and *"test"*.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.


---


## FashionMNIST

[Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) dataset.

```
from yupeeee_pytools.datasets import FashionMNIST

dataset = FashionMNIST(
    root: str,
    train: bool = True,
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **train** (*bool, optional*):
If *True*, creates dataset from training set, otherwise creates from test set.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.


---


## ImageNet

[ILSVRC2012](https://image-net.org/challenges/LSVRC/2012/index.php) dataset.
**The dataset must be downloaded in the *root* directory.**
To download the dataset, create your ImageNet account <sup>[link](https://image-net.org/signup.php)</sup>
and download the dataset <sup>[link](https://image-net.org/challenges/LSVRC/2012/2012-downloads.php)</sup>.

```
from yupeeee_pytools.datasets import ImageNet

dataset = ImageNet(
    root: str,
    split: str = "train",
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
)
```

### Parameters

- **root** (*string*):
Root directory of the ILSVRC2012 dataset.

- **split** (*string, optional*):
The dataset split; supports *"train"* (default), and *"val"*.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.


---


## MNIST

[MNIST](https://yann.lecun.com/exdb/mnist/) dataset.

```
from yupeeee_pytools.datasets import MNIST

dataset = MNIST(
    root: str,
    train: bool = True,
    transform: Optional[Callable] = default_transform,
    target_transform: Optional[Callable] = None,
    download: bool = False,
)
```

### Parameters

- **root** (*string*):
Root directory where the dataset exists or will be saved to if ***download*** is set to *True*.

- **train** (*bool, optional*):
If *True*, creates dataset from training set, otherwise creates from test set.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.

- **download** (*bool, optional*):
If *True*, downloads the dataset from the internet and puts it into the root directory.
If dataset is already downloaded, it is not downloaded again.
