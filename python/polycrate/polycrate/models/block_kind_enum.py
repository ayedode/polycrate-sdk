from typing import Literal

BlockKindEnum = Literal["dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"]

BLOCK_KIND_ENUM_VALUES: set[BlockKindEnum] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_block_kind_enum(value: str) -> BlockKindEnum:
    if value in BLOCK_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_KIND_ENUM_VALUES!r}")
