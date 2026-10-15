from typing import Literal

ActivityListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ACTIVITY_LIST_STATE_VALUES: set[ActivityListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_activity_list_state(value: str) -> ActivityListState:
    if value in ACTIVITY_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_LIST_STATE_VALUES!r}")
