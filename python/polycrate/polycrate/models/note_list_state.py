from typing import Literal

NoteListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTE_LIST_STATE_VALUES: set[NoteListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_note_list_state(value: str) -> NoteListState:
    if value in NOTE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_LIST_STATE_VALUES!r}")
