from typing import Literal

ApiV1NotesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_NOTES_LIST_STATE_VALUES: set[ApiV1NotesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_notes_list_state(value: str) -> ApiV1NotesListState:
    if value in API_V1_NOTES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_STATE_VALUES!r}")
