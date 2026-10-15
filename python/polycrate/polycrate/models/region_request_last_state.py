from typing import Literal

RegionRequestLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGION_REQUEST_LAST_STATE_VALUES: set[RegionRequestLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_region_request_last_state(value: str) -> RegionRequestLastState:
    if value in REGION_REQUEST_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_REQUEST_LAST_STATE_VALUES!r}")
