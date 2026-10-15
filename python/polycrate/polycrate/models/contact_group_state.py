from typing import Literal

ContactGroupState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONTACT_GROUP_STATE_VALUES: set[ContactGroupState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_contact_group_state(value: str) -> ContactGroupState:
    if value in CONTACT_GROUP_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_STATE_VALUES!r}")
