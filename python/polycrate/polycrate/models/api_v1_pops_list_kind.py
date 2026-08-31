from typing import Literal

ApiV1PopsListKind = Literal["datacenter", "datacenter-park", "region"]

API_V1_POPS_LIST_KIND_VALUES: set[ApiV1PopsListKind] = {
    "datacenter",
    "datacenter-park",
    "region",
}


def check_api_v1_pops_list_kind(value: str) -> ApiV1PopsListKind:
    if value in API_V1_POPS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_KIND_VALUES!r}")
