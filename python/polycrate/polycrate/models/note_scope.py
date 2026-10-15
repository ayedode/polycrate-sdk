from typing import Literal

NoteScope = Literal["system", "user"]

NOTE_SCOPE_VALUES: set[NoteScope] = {
    "system",
    "user",
}


def check_note_scope(value: str) -> NoteScope:
    if value in NOTE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_SCOPE_VALUES!r}")
