# yuptools.tools.linalgtools

Utility functions for performing linear algebra operations on vectors and tensors.


- [repeat_tensor](#repeat_tensor)
- [normalize_v](#normalize_v)
- [proj_v1_to_v2](#proj_v1_to_v2)
- [orthogonal_to_v](#orthogonal_to_v)
- [angle_of_three_points](#angle_of_three_points)


---


## repeat_tensor

Repeats a PyTorch tensor along a specified dimension.

```
repeated_tensor: torch.Tensor = repeat_tensor(
    tensor: torch.Tensor,
    repeat: int,
    dim: int = 0,
)
```

### Input

- **tensor** (*torch.Tensor*):
The input tensor to be repeated.

- **repeat** (*int*):
The number of times to repeat the tensor.

- **dim** (*int*):
The dimension along which to repeat the tensor.
Default is *0*.

### Output

- **repeated_tensor** (*torch.Tensor*):
The repeated tensor.


---


## normalize_v

Normalizes a vector (i.e., 1-dimensional PyTorch tensor).

```
normalized_v: torch.Tensor = normalize_v(
    v: torch.Tensor,
    p: Union[str, int] = "fro",
)
```

### Input

- **v** (*torch.Tensor*):
The input vector to be normalized.

- **p** (*str* or *int*):
The type of norm to use.
Can be a string (*"fro"* for Frobenius norm) or an integer indicating the p-norm.
Default is *"fro"*.

### Output

- **normalized_v** (*torch.Tensor*):
The normalized vector.


---


## proj_v1_to_v2

Calculates the projection of one vector (i.e., 1-dimensional PyTorch tensor) onto another.

```
projected_v: torch.Tensor = proj_v1_to_v2(
    v1: torch.Tensor,
    v2: torch.Tensor,
)
```

### Input

- **v1** (*torch.Tensor*):
The input vector to be projected.

- **v2** (*torch.Tensor*):
The vector onto which to project ***v1***.

### Output

- **projected_v** (*torch.Tensor*):
The projected vector.


---


## orthogonal_to_v

Generates a random vector orthogonal to a given vector (i.e., 1-dimensional PyTorch tensor).

```
orthogonal_v: torch.Tensor = orthogonal_to_v(
    v: torch.Tensor,
    seed: int = None,
)
```

### Input

- **v** (*torch.Tensor*):
The input vector.

- **seed** (*int, optional*):
The random seed to use for generating the orthogonal vector.
Default is *None*.

### Output

- **orthogonal_v** (*torch.Tensor*):
The orthogonal vector.


---


## angle_of_three_points

Calculates the angle between three points.

```
angle: float = angle_of_three_points(
    i: torch.Tensor,
    f1: torch.Tensor,
    f2: torch.Tensor,
    eps: float = 1e-7,
)
```

### Input

- **i** (*torch.Tensor*):
The initial point.

- **f1** (*torch.Tensor*):
The first final point.

- **f2** (*torch.Tensor*):
The second final point.

- **eps** (*float, optional*):
A small value added to the denominator to avoid division by zero.
Default is *1e-7*.

### Output

- **angle** (*float*):
The angle between the three points in radians.
