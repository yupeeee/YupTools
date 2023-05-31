# yuptools.train.trainer.SupervisedLearner

Python class for training models for supervised learning tasks.


- [Properties](#properties)
- Methods
  - [run](#run)
  - [resume](#resume)


---


```
SupervisedLearner(
    train_dataset,
    val_dataset,
    model,
    config_path: str,
    model_name: Optional[str],
    use_cuda: bool = False,
)
```

## Properties

- **train_dataset**:
The training dataset used for training the model.

- **val_dataset**:
The validation dataset used for evaluating the model.

- **model** (*torch.nn.Module*):
The model to be trained.

- **config_path** (*str*):
The path to the YAML configuration file.
To see an example of a YAML configuration file, go to
[**link**](../../src/yuptools/train/config_examples/imagenet_config.yaml).

- **model_name** (*str, optional*):
The name of the model.
Automatically initialized if not specified (i.e., set to *None*).
Default is *None*.

- **use_cuda** (*bool*):
Determines if CUDA should be used for training.
Default is *False*.


## Methods


### run

Runs the training and evaluation process.

- **weights_save_root** (*str*):
The root directory for saving model weights.

- **log_save_root** (*str*):
The root directory for saving training logs.

- **weights_save_period** (*int*):
The period at which to save model weights.
Default is *1*.

```
trainer = SupervisedLearner(...)

trainer.run(
    weights_save_root: str,
    log_save_root: str,
    weights_save_period: int = 1,
)
```


### resume

Resumes a previous training process from a checkpoint.

- **weights_save_root** (*str*):
The root directory where the model weights were saved.

- **log_save_root** (*str*):
The root directory where the training logs were saved.

- **prev_datetime** (*str*):
The date and time (train ID) of the previous training process.

- **weights_save_period** (*int*):
The period at which to save model weights.
Default is *1*.

```
trainer = SupervisedLearner(...)

trainer.resume(
    weights_save_root: str,
    log_save_root: str,
    prev_datetime: str,
    weights_save_period: int = 1,
)
```
