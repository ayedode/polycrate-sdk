from typing import Literal

ApiV1LoadbalancersRegionsListScope = Literal["system", "user"]

API_V1_LOADBALANCERS_REGIONS_LIST_SCOPE_VALUES: set[ApiV1LoadbalancersRegionsListScope] = {
    "system",
    "user",
}


def check_api_v1_loadbalancers_regions_list_scope(value: str) -> ApiV1LoadbalancersRegionsListScope:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_SCOPE_VALUES!r}")
