# yuptools.travel.footprint.Footprint

Performs decision boundary travel in the input space
by iteratively adjusting the input data along the specified direction.
For further understanding of the idea of *travel* and *direction*,
refer to [**link**](https://arxiv.org/abs/2210.05742).


- [Properties](#properties)
- Methods
  - [call](#call)


---


```
Traveler(
    step: int,
    model: torch.nn.Module,
    method: str = default_method,
    perp: bool = False,
    normalize: str = default_normalize,
    bound: bool = False,
    seed: int = default_seed,
    use_cuda: bool = False,
)
```

## Properties

- **step** (*int*):
The number of steps to generate footprints.

- **model** (*torch.nn.Module*):
PyTorch model for which footprints will be generated.

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

- **bound** (*bool*):
Determines if the generated footprints should be bound within a specific range,
i.e., [0, 1] for image data.
Default is *False*.

- **seed** (*int*):
Random seed for direction generation.
Default is *None*.

- **use_cuda** (*bool*):
Determines if CUDA should be used for direction generation.
Default is *False*.


## Methods


### *call*

Generates footprints for the given data and epsilons (and targets). \
**Note**: Negative epsilon values (default: *-1.*) will result in dummy footprints,
i.e., ***torch.ones_like(data) * negative_value (default: -1.)***.

- **data** (*torch.Tensor*):
Input data for which footprints will be generated.
It should be a tensor of shape (*batch_size*, ...),
where ... represents the shape of each data sample.

- **epsilons** (*torch.Tensor*):
Epsilon values for footprint generation.
It should be a 1-dimensional tensor of shape (*batch_size*, ).

- **targets** (*torch.Tensor, optional*):
Target of the input data.
It should be a 1-dimensional tensor of shape (*batch_size*, ).
Must be initialized for specific direction generation methods
(e.g., *"fgsm"*, *"fgsm-targeted"*).
Default is *None*.

```
footprints: torch.Tensor = Footprint(...)(
    data: torch.Tensor,
    epsilons: torch.Tensor,
    targets: torch.Tensor = None,
)
```