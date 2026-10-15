from typing import Literal

RegionRequestState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGION_REQUEST_STATE_VALUES: set[RegionRequestState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_region_request_state(value: str) -> RegionRequestState:
    if value in REGION_REQUEST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_REQUEST_STATE_VALUES!r}")
