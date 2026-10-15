from typing import Literal

BlockListKind = Literal["dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"]

BLOCK_LIST_KIND_VALUES: set[BlockListKind] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_block_list_kind(value: str) -> BlockListKind:
    if value in BLOCK_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_LIST_KIND_VALUES!r}")
