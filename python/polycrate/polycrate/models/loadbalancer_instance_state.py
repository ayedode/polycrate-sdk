from typing import Literal

LoadbalancerInstanceState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LOADBALANCER_INSTANCE_STATE_VALUES: set[LoadbalancerInstanceState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_loadbalancer_instance_state(value: str) -> LoadbalancerInstanceState:
    if value in LOADBALANCER_INSTANCE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LOADBALANCER_INSTANCE_STATE_VALUES!r}")
