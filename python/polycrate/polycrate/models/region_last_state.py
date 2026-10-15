from typing import Literal

RegionLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGION_LAST_STATE_VALUES: set[RegionLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_region_last_state(value: str) -> RegionLastState:
    if value in REGION_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_LAST_STATE_VALUES!r}")
