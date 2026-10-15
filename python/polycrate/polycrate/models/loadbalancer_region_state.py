from typing import Literal

LoadbalancerRegionState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LOADBALANCER_REGION_STATE_VALUES: set[LoadbalancerRegionState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_loadbalancer_region_state(value: str) -> LoadbalancerRegionState:
    if value in LOADBALANCER_REGION_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_STATE_VALUES!r}")
