from typing import Literal

ActivityState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ACTIVITY_STATE_VALUES: set[ActivityState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_activity_state(value: str) -> ActivityState:
    if value in ACTIVITY_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_STATE_VALUES!r}")
