from typing import Literal

EndpointState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ENDPOINT_STATE_VALUES: set[EndpointState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_endpoint_state(value: str) -> EndpointState:
    if value in ENDPOINT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_STATE_VALUES!r}")
