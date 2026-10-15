from typing import Literal

PatchedHostRequestKind = Literal["bare_metal", "vm"]

PATCHED_HOST_REQUEST_KIND_VALUES: set[PatchedHostRequestKind] = {
    "bare_metal",
    "vm",
}


def check_patched_host_request_kind(value: str) -> PatchedHostRequestKind:
    if value in PATCHED_HOST_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_HOST_REQUEST_KIND_VALUES!r}")
