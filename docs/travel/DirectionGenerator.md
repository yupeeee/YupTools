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
    seed: int = default_seed,
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

    - **"fgsm"**: generates direction using [FGSM](../attacks/FGSM.md).
    - **"fgsm_targeted"**: generates direction using [FGSM (targeted=True)](../attacks/FGSM.md).

- **perp** (*bool*):
Determines if the generated directions should be perpendicular to the original direction.
Default is *False*.

- **normalize** (*str*):
Specifies the method to normalize directions.
Available methods are listed below.
Default is *"dim"*.

    - **"dim"**: normalizes the direction $\mathrm{\mathbf{d}}$ as 
        $\|\mathrm{\mathbf{d}}\|_{2} = \sqrt{D}$,
        where $D$ is the dimension of $\mathrm{\mathbf{d}}$.
    - **"unit"**: normalizes the direction $\mathrm{\mathbf{d}}$ as 
        $\|\mathrm{\mathbf{d}}\|_{2} = 1$.

- **seed** (*int*):
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

- **targets** (*torch.Tensor, optional*):
Target of the input data.
Must be initialized for specific direction generation methods
(e.g., *"fgsm"*, *"fgsm-targeted"*).
Default is *None*.

```
directions: torch.Tensor = DirectionGenerator(...)(
    data: torch.Tensor,
    targets: torch.Tensor,
)
```
