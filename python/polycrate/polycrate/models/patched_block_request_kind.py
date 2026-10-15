from typing import Literal

PatchedBlockRequestKind = Literal[
    "dockerapp", "generic", "k8sapp", "k8sappinstance", "k8scluster", "library", "linuxapp"
]

PATCHED_BLOCK_REQUEST_KIND_VALUES: set[PatchedBlockRequestKind] = {
    "dockerapp",
    "generic",
    "k8sapp",
    "k8sappinstance",
    "k8scluster",
    "library",
    "linuxapp",
}


def check_patched_block_request_kind(value: str) -> PatchedBlockRequestKind:
    if value in PATCHED_BLOCK_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BLOCK_REQUEST_KIND_VALUES!r}")
