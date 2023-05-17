# yuptools.plotlib.common

Commonly used functions for plotting figures.


- [chw_to_hwc](#chw_to_hwc)
- [best_figsize_for_subplots](#best_figsize_for_subplots)


---


## chw_to_hwc

Permutes a given tensor with dimensions *(N×)C×H×W* to *(N×)H×W×C*.

```
_images: torch.Tensor = chw_to_hwc(images: torch.Tensor,)
```

### Input

- **images** (*torch.Tensor*):
Image(s) with dimensions *(N×)C×H×W*.

### Output

- **_images** (*torch.Tensor*):
Image(s) with dimensions *(N×)H×W×C*.


---


## best_figsize_for_subplots

Calculates the optimal height and width dimensions for a set of subplots in a grid layout,
given a desired aspect ratio and the total number of subplots.

```
best_hw: Tuple[int, int] = best_figsize_for_subplots(
    num_figs: int,
    desired_hw_ratio: Tuple[int, int] = (1, 1),
)
```

### Input

- **num_figs** (*int*):
Total number of subplots that need to be accommodated.

- **desired_hw_ratio** (*Tuple[int, int]*):
Desired aspect ratio of the subplots. Default is *(1, 1)*.

### Output

- **best_hw** (*Tuple[int, int]*):
The best height and width dimensions for the subplots.
