from typing import Literal

PopApiType = Literal["", "custom_rest", "none", "openstack", "proxmox"]

POP_API_TYPE_VALUES: set[PopApiType] = {
    "",
    "custom_rest",
    "none",
    "openstack",
    "proxmox",
}


def check_pop_api_type(value: str) -> PopApiType:
    if value in POP_API_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_API_TYPE_VALUES!r}")
