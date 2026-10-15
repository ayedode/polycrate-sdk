from typing import Literal

RegionListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

REGION_LIST_STATE_VALUES: set[RegionListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_region_list_state(value: str) -> RegionListState:
    if value in REGION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_LIST_STATE_VALUES!r}")
