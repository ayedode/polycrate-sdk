from typing import Literal

LoadbalancerRegionLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LOADBALANCER_REGION_LAST_STATE_VALUES: set[LoadbalancerRegionLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_loadbalancer_region_last_state(value: str) -> LoadbalancerRegionLastState:
    if value in LOADBALANCER_REGION_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_REGION_LAST_STATE_VALUES!r}")
