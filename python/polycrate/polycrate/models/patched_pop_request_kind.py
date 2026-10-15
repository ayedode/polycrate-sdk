from typing import Literal

PatchedPopRequestKind = Literal["datacenter", "datacenter-park", "region"]

PATCHED_POP_REQUEST_KIND_VALUES: set[PatchedPopRequestKind] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_patched_pop_request_kind(value: str) -> PatchedPopRequestKind:
    if value in PATCHED_POP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_KIND_VALUES!r}")
