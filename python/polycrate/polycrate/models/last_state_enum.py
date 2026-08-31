from typing import Literal

LastStateEnum = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

LAST_STATE_ENUM_VALUES: set[LastStateEnum] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_last_state_enum(value: str) -> LastStateEnum:
    if value in LAST_STATE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LAST_STATE_ENUM_VALUES!r}")
