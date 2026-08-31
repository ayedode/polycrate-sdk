from typing import Literal

ApiV1LoadbalancersInstancesListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_NOT_VALUES: set[ApiV1LoadbalancersInstancesListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_loadbalancers_instances_list_state_not(value: str) -> ApiV1LoadbalancersInstancesListStateNot:
    if value in API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_INSTANCES_LIST_STATE_NOT_VALUES!r}"
    )
