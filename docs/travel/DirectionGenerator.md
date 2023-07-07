# yuptools.travel.direction.DirectionGenerator

Generates travel directions based on specified methods using a given model.
For further understanding of the idea of *travel* and *direction*,
refer to [**link**](https://arxiv.org/abs/2210.05742).


- [Properties](#properties)
- Methods
  - [call](#call)


---


```
DirectionGenerator(
    model: Optional[torch.nn.Module] = None,
    method: str = default_method,
    perp: bool = False,
    normalize: str = default_normalize,
    seed: Optional[int] = default_seed,
    use_cuda: bool = False,
)
```

## Properties

- **model** (*torch.nn.Module, optional*):
PyTorch model used for direction generation.
Must be initialized for specific direction generation methods
(e.g., *"fgsm"*, *"fgsm-targeted"*).
Default is *None*.

- **method** (*str*):
Method for generating directions.
Available methods are listed below.
Default is *"fgsm"*.

    - **"custom"**: Generates a custom direction for given input data and destinations.
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

- **seed** (*int, optional*):
Random seed for direction generation.
Default is *None*.

- **use_cuda** (*bool*):
Determines if CUDA should be used for direction generation.
Default is *False*.


## Methods


### *call*

Generates travel directions based on the specified method and input data (and targets).

- **data** (*torch.Tensor*):
Input data to be traveled.
It should be a tensor of shape (*batch_size*, ...),
where ... represents the shape of each data sample.

- **targets** (*torch.Tensor, optional*):
Target of the input data.
It should be a 1-dimensional tensor of shape (*batch_size*, ).
Must be initialized for specific direction generation methods
(e.g., *"fgsm"*, *"fgsm-targeted"*).
Default is *None*.

- **destinations** (*torch.Tensor, optional*):
Destinations of the input data in the input space.
It should be a tensor with the same shape as ***data***.
It is only required as input when the selected method for generating directions is *"custom"*.
Default is *None*.

```
directions: torch.Tensor = DirectionGenerator(...)(
    data: torch.Tensor,
    targets: Optional[torch.Tensor] = None,
    destinations: Optional[torch.Tensor] = None,
)
```
