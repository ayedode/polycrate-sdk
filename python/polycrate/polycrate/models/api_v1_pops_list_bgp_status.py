from typing import Literal

ApiV1PopsListBgpStatus = Literal["no", "planned", "unknown", "yes"]

API_V1_POPS_LIST_BGP_STATUS_VALUES: set[ApiV1PopsListBgpStatus] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_api_v1_pops_list_bgp_status(value: str) -> ApiV1PopsListBgpStatus:
    if value in API_V1_POPS_LIST_BGP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_BGP_STATUS_VALUES!r}")
