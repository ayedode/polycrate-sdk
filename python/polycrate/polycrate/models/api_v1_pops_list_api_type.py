from typing import Literal

ApiV1PopsListApiType = Literal["custom_rest", "none", "openstack", "proxmox"]

API_V1_POPS_LIST_API_TYPE_VALUES: set[ApiV1PopsListApiType] = {
    "custom_rest",
    "none",
    "openstack",
    "proxmox",
}


def check_api_v1_pops_list_api_type(value: str) -> ApiV1PopsListApiType:
    if value in API_V1_POPS_LIST_API_TYPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_API_TYPE_VALUES!r}")
