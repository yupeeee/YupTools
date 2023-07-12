# yuptools.tools.imgtools

Utility functions for working with images.


- [image_entropy](#image_entropy)


---


## image_entropy

Calculates the entropy of an input image.

```
entropy: float, entropy_mat: torch.Tensor = image_entropy(
    image: torch.Tensor,
    method: str = "rgb",
)
```

### Input

- **image** (*torch.Tensor*):
The input image as a PyTorch tensor.
The image can be either grayscale (H\*W) or RGB (C\*H\*W).

- **method** (*str*):
The method used to calculate the entropy.
It can be either *"rgb"* or *"gray"*.
Default is *"gray"*.

### Output

- **entropy** (*float*):
The entropy value of the image.

- **entropy_mat** (*torch.Tensor*):
The entropy matrix, which has the same shape as the input image (without channels; H\*W).
