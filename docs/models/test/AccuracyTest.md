# yuptools.models.test.accuracy.AccuracyTest

Evaluates the accuracy of a given model on a dataset.

- [Properties](#properties)
- Methods
  - [call](#call)


---


```
AccuracyTest(
    top_k: int = 1,
    batch_size: int = 64,
    use_cuda: bool = False,
    verbose: bool = False,
)
```

## Properties

- **top_k** (*int*):
The value of k for top-k accuracy computation.
Default is *1*.

- **batch_size** (*int, optional*):
The batch size for data loading.
Default is *64*.

- **use_cuda** (*bool*):
Determines if CUDA should be used for computation.
Default is *False*.

- **verbose** (*bool*):
Determines if progress information should be displayed.
Default is *False*.


## Methods


### *call*

Performs the top-k accuracy test on the given model.

```
from torchvision import transforms as tf

from yuptools.datasets import ImageNet, image_classification_transforms
from yuptools.models import ImageNetClassificationModel, default_weights, \
    AccuracyTest


IMAGENET_DIR = ...
k = 1

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

test = AccuracyTest(
    top_k=k,
    batch_size=32,
    use_cuda=True,
    verbose=True,
)

acc = test(dataset, model.model)
print(f"acc@{k} of {model.name} on {dataset.name}: {acc * 100:.2f}%")

>>> Accuracy Test: 100%|██████████| 1563/1563 [10:11<00:00,  2.55it/s]
    acc@1 of resnet50 on ImageNet: 72.97%
```
