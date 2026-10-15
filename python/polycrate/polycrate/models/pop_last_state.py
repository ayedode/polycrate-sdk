from typing import Literal

PopLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

POP_LAST_STATE_VALUES: set[PopLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pop_last_state(value: str) -> PopLastState:
    if value in POP_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_LAST_STATE_VALUES!r}")
