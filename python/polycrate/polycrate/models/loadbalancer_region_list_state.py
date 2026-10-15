from typing import Literal

LoadbalancerRegionListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LOADBALANCER_REGION_LIST_STATE_VALUES: set[LoadbalancerRegionListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_loadbalancer_region_list_state(value: str) -> LoadbalancerRegionListState:
    if value in LOADBALANCER_REGION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_LIST_STATE_VALUES!r}")
