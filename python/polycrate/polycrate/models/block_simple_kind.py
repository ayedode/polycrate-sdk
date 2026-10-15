from typing import Literal

BlockSimpleKind = Literal["dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"]

BLOCK_SIMPLE_KIND_VALUES: set[BlockSimpleKind] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_block_simple_kind(value: str) -> BlockSimpleKind:
    if value in BLOCK_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_SIMPLE_KIND_VALUES!r}")
