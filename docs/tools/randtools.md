# yuptools.tools.randtools

Utility functions for working with random number generations.


- [set_random_seed](#set_random_seed)


---


## set_random_seed

Ensures reproducibility in random number generation across different runs of the code.

```
set_random_seed(seed: int = None,)
```

### Input

- **seed** (*int*):
The seed value to set for random number generation.
If not provided, i.e., set as *None*, the random seed will not be set.
Default is *None*.

### Output

- *None*
