from typing import Literal

ApiV1ContactsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CONTACTS_LIST_STATE_VALUES: set[ApiV1ContactsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_contacts_list_state(value: str) -> ApiV1ContactsListState:
    if value in API_V1_CONTACTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTS_LIST_STATE_VALUES!r}")
