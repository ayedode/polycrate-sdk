from typing import Literal

PopRequestApiType = Literal["", "custom_rest", "none", "openstack", "proxmox"]

POP_REQUEST_API_TYPE_VALUES: set[PopRequestApiType] = {
    "",
    "custom_rest",
    "none",
    "openstack",
    "proxmox",
}


def check_pop_request_api_type(value: str) -> PopRequestApiType:
    if value in POP_REQUEST_API_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_API_TYPE_VALUES!r}")
