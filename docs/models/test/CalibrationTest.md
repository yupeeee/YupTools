# yuptools.models.test.calibration.CalibrationTest

Evaluates the calibration of a given model on a dataset
using the Expected Calibration Error (ECE)
and signed Expected Calibration Error (sECE) metrics.

ECE and sECE are computed as follows:
$$\mathrm{ECE} = \sum_ {i=1}^{K}{P(i)\cdot|o_ {i}-e_ {i}|},$$
$$\mathrm{sECE} = \sum_ {i=1}^{K}{P(i)\cdot(o_ {i}-e_ {i})},$$
where $K$ is the number of bins of confidence,
$P(i)$ is the fraction of data falling into bin $i$,
$o_ {i}$ is the accuracy of the data in bin $i$,
and $e_ {i}$ is the average confidence of the data in bin $i$.

- [Properties](#properties)
- Methods
  - [call](#call)


---


```
CalibrationTest(
    num_bins: int = 10,
    batch_size: int = 64,
    use_cuda: bool = False,
    verbose: bool = False,
)
```

## Properties

- **num_bins** (*int*):
The number of bins ($K$) to use for computing calibration metrics.
Default is *10*.

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

Performs the calibration test on the given model.

```
from torchvision import transforms as tf

from yuptools.datasets import ImageNet, image_classification_transforms
from yuptools.models import ImageNetClassificationModel, default_weights, \
    CalibrationTest


IMAGENET_DIR = ...
num_bins = 10

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

test = CalibrationTest(
    num_bins=num_bins,
    batch_size=32,
    use_cuda=True,
    verbose=True,
)

ece_data = test(dataset, model.model)

print(f"Calibration test result of {model.name} on {dataset.name}:")
for key, value in ece_data.items():
    print(f"[{key}] {value}")

>>> Calibration Test: 100%|██████████| 1563/1563 [10:10<00:00,  2.56it/s]
    Calibration test result of resnet50 on ImageNet:
    [num_data] 50000
    [bins] tensor([0.0000, 0.1000, 0.2000, 0.3000, 0.4000, 0.5000, ...])
    [bin_sizes] [431, 1547, 2100, 2607, 2984, 3625, 3418, 3518, 4628, 25142]
    [mid_confs] [tensor(0.0500), tensor(0.1500), tensor(0.2500), ...]
    [avg_confs] [tensor(0.0738), tensor(0.1546), tensor(0.2509), ...]
    [accs] [0.08120649651972157, 0.13703943115707823, 0.2580952380952381, ...]
    [ECE] 0.04164934158325195
    [sECE] -0.04091877490282059
```
