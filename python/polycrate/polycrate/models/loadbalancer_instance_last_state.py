from typing import Literal

LoadbalancerInstanceLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LOADBALANCER_INSTANCE_LAST_STATE_VALUES: set[LoadbalancerInstanceLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_loadbalancer_instance_last_state(value: str) -> LoadbalancerInstanceLastState:
    if value in LOADBALANCER_INSTANCE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_LAST_STATE_VALUES!r}")
