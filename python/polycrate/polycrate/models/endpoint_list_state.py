from typing import Literal

EndpointListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ENDPOINT_LIST_STATE_VALUES: set[EndpointListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_endpoint_list_state(value: str) -> EndpointListState:
    if value in ENDPOINT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENDPOINT_LIST_STATE_VALUES!r}")
