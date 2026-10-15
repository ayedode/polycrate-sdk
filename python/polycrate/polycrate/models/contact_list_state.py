from typing import Literal

ContactListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONTACT_LIST_STATE_VALUES: set[ContactListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_contact_list_state(value: str) -> ContactListState:
    if value in CONTACT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_LIST_STATE_VALUES!r}")
