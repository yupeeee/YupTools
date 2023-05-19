__all__ = [
    "default_weights",
    "not_in_pytorch_weights_dir",
    "modes",
    "default_mode",
    "not_in_pytorch_models",
]

default_weights = "IMAGENET1K_V1"
not_in_pytorch_weights_dir = "./src/yuptools/models/classification/not_in_pytorch_weights"
modes = [None, "train", "eval", ]
default_mode = None

not_in_pytorch_models = {
    "deit_tiny_patch16_224": "DeiT-Ti",
    "deit_small_patch16_224": "DeiT-S",
    "deit_base_patch16_224": "DeiT-B",
    "deit_tiny_distilled_patch16_224": "DeiT-Ti⚗",
    "deit_small_distilled_patch16_224": "DeiT-S⚗",
    "deit_base_distilled_patch16_224": "DeiT-B⚗",
    "deit_base_patch16_384": "DeiT-B↑384",
    "deit_base_distilled_patch16_384": "DeiT-B⚗↑384",

    "mixer_b_16": "Mixer-B_16",
    "mixer_l_16": "Mixer-L_16",

    "poolformer_s12": "PoolFormer-S12",
    "poolformer_s24": "PoolFormer-S24",
    "poolformer_s36": "PoolFormer-S36",
    "poolformer_m36": "PoolFormer-M36",
    "poolformer_m48": "PoolFormer-M48",

    "pvt_tiny": "PVT-Tiny",
    "pvt_small": "PVT-Small",
    "pvt_medium": "PVT-Medium",
    "pvt_large": "PVT-Large",
}
