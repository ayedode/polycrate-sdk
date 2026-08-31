from typing import Literal

ApiV1LoadbalancersInstancesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_VALUES: set[ApiV1LoadbalancersInstancesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_loadbalancers_instances_list_state(value: str) -> ApiV1LoadbalancersInstancesListState:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_VALUES!r}")
