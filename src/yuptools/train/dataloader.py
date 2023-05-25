from torch.utils.data import DataLoader

__all__ = [
    "build_dataloader",
]


def build_dataloader(
        dataset,
        config,
) -> DataLoader:
    """
    in config.yaml:
    ⋮
    DATALOADER:
      BATCH_SIZE: int
      SHUFFLE: bool
      NUM_WORKERS: int
    ⋮
    """
    return DataLoader(
        dataset=dataset,
        batch_size=config.DATALOADER.BATCH_SIZE,
        shuffle=config.DATALOADER.SHUFFLE,
        num_workers=config.DATALOADER.NUM_WORKERS,
    )
