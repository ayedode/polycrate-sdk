from typing import Literal

BlockKind = Literal["dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"]

BLOCK_KIND_VALUES: set[BlockKind] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_block_kind(value: str) -> BlockKind:
    if value in BLOCK_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_KIND_VALUES!r}")
