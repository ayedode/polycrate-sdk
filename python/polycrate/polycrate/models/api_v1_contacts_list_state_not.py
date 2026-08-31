from typing import Literal

ApiV1ContactsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CONTACTS_LIST_STATE_NOT_VALUES: set[ApiV1ContactsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_contacts_list_state_not(value: str) -> ApiV1ContactsListStateNot:
    if value in API_V1_CONTACTS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_STATE_NOT_VALUES!r}")
