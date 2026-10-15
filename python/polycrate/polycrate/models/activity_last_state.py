from typing import Literal

ActivityLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ACTIVITY_LAST_STATE_VALUES: set[ActivityLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_activity_last_state(value: str) -> ActivityLastState:
    if value in ACTIVITY_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ACTIVITY_LAST_STATE_VALUES!r}")
