from typing import Literal

ContactState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONTACT_STATE_VALUES: set[ContactState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_contact_state(value: str) -> ContactState:
    if value in CONTACT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_STATE_VALUES!r}")
