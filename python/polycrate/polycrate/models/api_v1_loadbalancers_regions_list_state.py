from typing import Literal

ApiV1LoadbalancersRegionsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_LOADBALANCERS_REGIONS_LIST_STATE_VALUES: set[ApiV1LoadbalancersRegionsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_loadbalancers_regions_list_state(value: str) -> ApiV1LoadbalancersRegionsListState:
    if value in API_V1_LOADBALANCERS_REGIONS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_LIST_STATE_VALUES!r}")
