from typing import Literal

NoteState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

NOTE_STATE_VALUES: set[NoteState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_note_state(value: str) -> NoteState:
    if value in NOTE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_STATE_VALUES!r}")
