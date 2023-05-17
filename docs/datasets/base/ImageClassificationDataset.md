# yuptools.datasets.base.ImageClassificationDataset

Base structure for loading datasets used in image classification tasks.


- [Parameters](#parameters)
- [Attributes](#attributes)
- Methods
  - [\__getitem\__](#getitem)
  - [\__len\__](#len)
  - [make_dataset](#make_dataset)
  - [initialize](#initialize)
  - [data_and_targets_of_class_c](#data_and_targets_of_class_c)
  - [mean_and_std_of_data](#mean_and_std_of_data)


---


```
ImageClassificationDataset(
    name: str,
    transform: Optional[Callable] = torchvision.transforms.ToTensor(),
    target_transform: Optional[Callable] = None,
)
```

## Parameters

- **name** (*string*):
Name of the dataset.

- **transform** (*callable, optional*):
A function/transform that takes in a PIL image or a numpy.ndarray and returns its transformed version.
The transformation result must be of the type *torch.Tensor*.

- **target_transform** (*callable, optional*):
A function/transform that takes in the target and transforms it.


## Attributes

- **data** (*None*, must be initialized):
Data of dataset;
either the data itself (e.g., PIL image, numpy.ndarray, torch.Tensor)
or a list of tuples containing ***path_to_data** (str)* and ***target** (int)*.

- **targets** (*None*, must be initialized):
Targets of dataset.

- **class_labels** (*None*, must be initialized):
Class labels of dataset.


## Methods


### *\__getitem\__*

Returns the data and target at the given index of the dataset.

```
dataset = ImageClassificationDataset()
data: Any, target: Any = dataset[index: int]
```


### *\__len\__*

Returns the number of samples in the dataset.

```
dataset = ImageClassificationDataset()
length_of_dataset: int = len(dataset)
```


### make_dataset

Generates a list of samples of a form (path_to_data, target).

```
dataset = ImageClassificationDataset()
path_and_class: List[Tuple[str, int]] = \
    dataset.make_dataset(
        directory: str,
        extensions: List[str],
    )
```


### initialize

Initializes the dataset with the given data, targets, and class labels.


### data_and_targets_of_class_c

Returns the data and target for a specific class.

```
dataset = ImageClassificationDataset()
data_c: Any, targets_c: Any = \
    dataset.data_and_targets_of_class_c(c: int)
```


### mean_and_std_of_data

Calculates the mean and standard deviation of the data in the dataset.
**Raises an error if type(dataset.data) == list.**

```
dataset = ImageClassificationDataset()
data_c: Any, targets_c: Any = \
    dataset.data_and_targets_of_class_c(c: int)
```
