from typing import Literal

ApiV1PopsListIpv6Status = Literal["no", "planned", "unknown", "yes"]

API_V1_POPS_LIST_IPV_6_STATUS_VALUES: set[ApiV1PopsListIpv6Status] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_api_v1_pops_list_ipv_6_status(value: str) -> ApiV1PopsListIpv6Status:
    if value in API_V1_POPS_LIST_IPV_6_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_IPV_6_STATUS_VALUES!r}")
