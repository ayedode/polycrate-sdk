from typing import Literal

RegionState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGION_STATE_VALUES: set[RegionState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_region_state(value: str) -> RegionState:
    if value in REGION_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_STATE_VALUES!r}")
