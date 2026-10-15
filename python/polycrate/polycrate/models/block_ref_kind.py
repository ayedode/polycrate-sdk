from typing import Literal

BlockRefKind = Literal["dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"]

BLOCK_REF_KIND_VALUES: set[BlockRefKind] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_block_ref_kind(value: str) -> BlockRefKind:
    if value in BLOCK_REF_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_REF_KIND_VALUES!r}")
