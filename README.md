# YupTools

YupTools is a Python package based on PyTorch.

---


## Installation

Latest version: 0.1.8 <br>
**Note: [Manual installation of PyTorch](https://pytorch.org/get-started/locally/) is required.**
```
pip install yuptools==0.1.8
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
scipy
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
    - [FGSM](https://github.com/yupeeee/YupTools/blob/main/docs/attacks/FGSM.md)
    - [IFGSM](https://github.com/yupeeee/YupTools/blob/main/docs/attacks/IFGSM.md)

- datasets
    - [base](https://github.com/yupeeee/YupTools/blob/main/docs/datasets/base.md)
    - [image_classification](https://github.com/yupeeee/YupTools/blob/main/docs/datasets/image_classification.md)

- models
    - classification
        - [base](https://github.com/yupeeee/YupTools/blob/main/docs/models/classification/base.md)
        - [models](https://github.com/yupeeee/YupTools/blob/main/docs/models/classification/models.md)
    - replace
        - [Replacer](https://github.com/yupeeee/YupTools/blob/main/docs/models/replace/base/Replacer.md)
    - test
        - [AccuracyTest](https://github.com/yupeeee/YupTools/blob/main/docs/models/test/AccuracyTest.md)
        - [CalibrationTest](https://github.com/yupeeee/YupTools/blob/main/docs/models/test/CalibrationTest.md)
        - [LinearityTest](https://github.com/yupeeee/YupTools/blob/main/docs/models/test/LinearityTest.md)
    - [xray (FeatureExtractor)](https://github.com/yupeeee/YupTools/blob/main/docs/models/xray.md)

- plotlib
    - [BarPlot](https://github.com/yupeeee/YupTools/blob/main/docs/plotlib/BarPlot.md)
    - [common](https://github.com/yupeeee/YupTools/blob/main/docs/plotlib/common.md)

- tools
    - [attrtools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/attrtools.md)
    - [dictools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/dictools.md)
    - [imgtools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/imgtools.md)
    - [linalgtools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/linalgtools.md)
    - [listools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/listools.md)
    - [pathtools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/pathtools.md)
    - [randtools](https://github.com/yupeeee/YupTools/blob/main/docs/tools/randtools.md)

- train
    - [SupervisedLearner](https://github.com/yupeeee/YupTools/blob/main/docs/train/SupervisedLearner.md)

- travel
    - [DirectionGenerator](https://github.com/yupeeee/YupTools/blob/main/docs/travel/DirectionGenerator.md)
    - [Footprint](https://github.com/yupeeee/YupTools/blob/main/docs/travel/Footprint.md)
    - [Traveler](https://github.com/yupeeee/YupTools/blob/main/docs/travel/Traveler.md)

- web
    - [ChromeDriver](https://github.com/yupeeee/YupTools/blob/main/docs/web/chrome/driver/ChromeDriver.md)
