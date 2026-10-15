from typing import Literal

ContactGroupListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CONTACT_GROUP_LIST_STATE_VALUES: set[ContactGroupListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_contact_group_list_state(value: str) -> ContactGroupListState:
    if value in CONTACT_GROUP_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTACT_GROUP_LIST_STATE_VALUES!r}")
