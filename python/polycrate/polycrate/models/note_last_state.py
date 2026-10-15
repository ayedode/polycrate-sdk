from typing import Literal

NoteLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTE_LAST_STATE_VALUES: set[NoteLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_note_last_state(value: str) -> NoteLastState:
    if value in NOTE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_LAST_STATE_VALUES!r}")
