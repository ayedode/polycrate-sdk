from typing import Literal

BlockRequestKind = Literal["dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"]

BLOCK_REQUEST_KIND_VALUES: set[BlockRequestKind] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_block_request_kind(value: str) -> BlockRequestKind:
    if value in BLOCK_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BLOCK_REQUEST_KIND_VALUES!r}")
