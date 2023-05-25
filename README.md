# YupTools

YupTools is a Python package based on PyTorch.

---


## Installation

Latest version: 0.1.1 <br>
**Note: [Manual installation of PyTorch](https://pytorch.org/get-started/locally/) is required.**
```
pip install yuptools==0.1.1
```


### Requirements

```
Python >= 3.8

matplotlib
numpy
pandas
Pillow
pyyaml
pyperclip
selenium
timm
# torch
# torchvision
tqdm
webdriver_manager
```


## Usage

```
import yuptools
```


## Structure

- attacks
    - [FGSM](./docs/attacks/FGSM.md)
    - [IFGSM](./docs/attacks/IFGSM.md)

- datasets
    - [base](./docs/datasets/base.md)
    - [image_classification](./docs/datasets/image_classification.md)

- models
    - classification
        - [base](./docs/models/classification/base.md)
        - [models](./docs/models/classification/models.md)
    - replace
        - [Replacer](docs/models/replace/base/Replacer.md)
    - test
        - [AccuracyTest](docs/models/test/AccuracyTest.md)
        - [CalibrationTest](docs/models/test/CalibrationTest.md)
        - [LinearityTest](docs/models/test/LinearityTest.md)
    - [xray (FeatureExtractor)](./docs/models/xray.md)

- plotlib
    - [common](./docs/plotlib/common.md)

- tools
    - [attrtools](./docs/tools/attrtools.md)
    - [dictools](./docs/tools/dictools.md)
    - [linalgtools](./docs/tools/linalgtools.md)
    - [listools](./docs/tools/listools.md)
    - [pathtools](./docs/tools/pathtools.md)
    - [randtools](./docs/tools/randtools.md)

- train
    - [SupervisedLearner](./docs/train/SupervisedLearner.md)

- travel
    - [DirectionGenerator](./docs/travel/DirectionGenerator.md)
    - [Footprint](./docs/travel/Footprint.md)
    - [Traveler](./docs/travel/Traveler.md)

- web
    - [ChromeDriver](./docs/web/chrome/driver/ChromeDriver.md)
