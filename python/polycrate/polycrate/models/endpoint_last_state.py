from typing import Literal

EndpointLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ENDPOINT_LAST_STATE_VALUES: set[EndpointLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_endpoint_last_state(value: str) -> EndpointLastState:
    if value in ENDPOINT_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_LAST_STATE_VALUES!r}")
