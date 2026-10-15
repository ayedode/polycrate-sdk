from typing import Literal

PopState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

POP_STATE_VALUES: set[PopState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pop_state(value: str) -> PopState:
    if value in POP_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_STATE_VALUES!r}")
