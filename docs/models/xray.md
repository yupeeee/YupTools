# yuptools.models.xray

Provides functionality for extracting features from a PyTorch model.


- [get_layer_ids](#get_layer_ids)
- [get_layer](#get_layer)
</br></br>
- [FeatureExtractor](#FeatureExtractor)


---


## get_layer_ids

Retrieves a list of layer IDs from a PyTorch model.

```
layer_ids: List[str] = get_layer_ids(model: torch.nn.Module,)
```

### Input

- **model** (*torch.nn.Module*):
The PyTorch model.

### Output

- **layer_ids** (*list*):
A list of layer IDs.


---


## get_layer

Retrieves a specific layer from a PyTorch model.

```
layer: torch.nn.Module = get_layer(
    model: torch.nn.Module,
    layer_id: str,
)
```

### Input

- **model** (*torch.nn.Module*):
The PyTorch model.

- **layer_id** (*str*):
The ID of the layer.

### Output

- **layer** (*torch.nn.Module*):
The requested layer.


---


## FeatureExtractor

A PyTorch module that facilitates feature extraction from a model.

```
feature_extractor: torch.nn.Module = FeatureExtractor(
    model: torch.nn.Module,
)
```

### Parameters

- **model** (*torch.nn.Module*):
The PyTorch model.

### *forward*

Performs a forward pass through the model and returns the extracted features.

```
features: Dict[str, torch.Tensor] = FeatureExtractor(
    model: torch.nn.Module,
)(x: torch.Tensor,)
```

- **x** (*torch.Tensor*):
The input tensor.

- **features** (*dict*):
Dictionary containing the extracted features.
The keys of the dictionary are layer IDs, and the values are the corresponding output tensors.
