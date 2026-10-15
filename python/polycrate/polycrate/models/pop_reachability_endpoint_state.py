from typing import Literal

PopReachabilityEndpointState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

POP_REACHABILITY_ENDPOINT_STATE_VALUES: set[PopReachabilityEndpointState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pop_reachability_endpoint_state(value: str) -> PopReachabilityEndpointState:
    if value in POP_REACHABILITY_ENDPOINT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REACHABILITY_ENDPOINT_STATE_VALUES!r}")
