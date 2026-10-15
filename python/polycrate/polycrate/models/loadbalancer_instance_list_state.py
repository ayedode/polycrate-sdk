from typing import Literal

LoadbalancerInstanceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LOADBALANCER_INSTANCE_LIST_STATE_VALUES: set[LoadbalancerInstanceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_loadbalancer_instance_list_state(value: str) -> LoadbalancerInstanceListState:
    if value in LOADBALANCER_INSTANCE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_LIST_STATE_VALUES!r}")
