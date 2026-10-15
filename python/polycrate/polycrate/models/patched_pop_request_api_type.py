from typing import Literal

PatchedPopRequestApiType = Literal["", "custom_rest", "none", "openstack", "proxmox"]

PATCHED_POP_REQUEST_API_TYPE_VALUES: set[PatchedPopRequestApiType] = {
    "",
    "custom_rest",
    "none",
    "openstack",
    "proxmox",
}


def check_patched_pop_request_api_type(value: str) -> PatchedPopRequestApiType:
    if value in PATCHED_POP_REQUEST_API_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_API_TYPE_VALUES!r}")
