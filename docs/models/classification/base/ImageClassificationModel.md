# yuptools.models.base.ImageClassificationModel

Base structure to handle a classification model for image classification tasks.
It provides functionalities for loading and using pre-trained models, making predictions, and accessing model layers.


- [Properties](#properties)
- [Attributes](#attributes)
- Methods
  - [call](#call)
  - [clean_name](#clean_name)
  - [load_state_dict](#load_state_dict)
  - [merge_preprocess](#merge_preprocess)
  - [predict](#predict)
  - [get_layer_ids](#get_layer_ids)
  - [get_layer](#get_layer)
  - [get_layer_weights](#get_layer_weights)


---


```
ImageClassificationModel(
    name: str,
    pretrained: bool = False,
    weights: Optional[str] = default_weights,
    weights_dir: Optional[str] = None,
    mode: str = default_mode,
    use_cuda: bool = False,
)
```

## Properties

- **name** (*str*):
Name of the model.

- **pretrained** (*bool*):
Specifies whether to load pretrained weights for the model.
Default is *False*.

- **weights** (*str*):
Specifies which pretrained weights to use for models supported by PyTorch.
See ***Table of all available classification weights*** in [**link**](https://pytorch.org/vision/stable/models.html) for more details, and possible values.
Default is *"IMAGENET1K_V1"*.

- **weights_dir** (*str*):
Directory to search for the pretrained weights of models unsupported by PyTorch.
**Must be initialized if loading a model unsupported by PyTorch**.

- **mode** (*str*):
Mode of the model.
Must be one of *[None, "train", "eval", ]*.
Default is *None*.

- **use_cuda** (*bool*):
Specifies whether to use CUDA for GPU acceleration.
Default is *False*.


## Attributes

- **model** (*torch.nn.Module*):
The loaded image classification model.


## Methods


### *call*

Executes the forward pass of the model on the input ***x***.
The input is moved to the appropriate device (CPU or GPU) based on the ***use_cuda*** property.
The output of the model is returned.

```
model = ImageClassificationModel(...)

y: Any = model(x: Any)
```


### clean_name

Cleans the model name by preserving capital letters.

```
model = ImageClassificationModel(name="resnet50", ...)

clean_name: str = model.clean_name()
print(clean_name)
>>> ResNet50
```


### load_state_dict

Loads the model's state dictionary from a file.

```
model = ImageClassificationModel(pretrained=False, ...)

model.load_state_dict(
    state_dict_path: str,
)
```


### merge_preprocess

Merges a pre-processing module with the model.

```
model = ImageClassificationModel(...)

model.merge_preprocess(
    preprocess: torch.nn.Module,
)
```


### predict

Performs classification on the input data and returns the predicted labels and confidence scores.

```
model = ImageClassificationModel(...)

preds, confs = model.predict(
    x: Any,
)
```


### get_layer_ids

Retrieves the IDs of all the layers in the model.

```
model = ImageClassificationModel(name="resnet50", ...)

layer_ids: List[str] = model.get_layer_ids()
print(layer_ids)
>>> ['conv1', 'bn1', 'relu', 'maxpool', 'layer1.0.conv1', ...]
```


### get_layer

Retrieves a specific layer from the model.

```
model = ImageClassificationModel(name="resnet50", ...)

# retrieve layer using index
layer: torch.nn.Module = model.get_layer(0)
print(layer)
>>> Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)

# retrieve layer using layer ID
layer: torch.nn.Module = model.get_layer("conv1")
print(layer)
>>> Conv2d(3, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
```


### get_layer_weights

Retrieves the weights of a specific layer from the model.
Returns *None* if the layer has no weights.

```
model = ImageClassificationModel(name="resnet50", ...)

# retrieve layer weights using index
weights: torch.Tensor = model.get_layer_weights(0)
print(weights)
>>> tensor([[[[ 1.3335e-02,  1.4664e-02, -1.5351e-02,  ..., -4.0896e-02,
              ...
              6.7615e-02, -6.7650e-03]]]])

# retrieve layer weights using layer ID
weights: torch.Tensor = model.get_layer("conv1")
print(weights)
>>> tensor([[[[ 1.3335e-02,  1.4664e-02, -1.5351e-02,  ..., -4.0896e-02,
              ...
              6.7615e-02, -6.7650e-03]]]])
```
