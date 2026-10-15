from typing import Literal

NoteKind = Literal[
    "app-release",
    "comment",
    "info",
    "meeting",
    "news",
    "object-note",
    "post-mortem",
    "provider-status",
    "reminder",
    "restore-test",
    "todo",
    "warning",
]

NOTE_KIND_VALUES: set[NoteKind] = {
    "app-release",
    "comment",
    "info",
    "meeting",
    "news",
    "object-note",
    "post-mortem",
    "provider-status",
    "reminder",
    "restore-test",
    "todo",
    "warning",
}


def check_note_kind(value: str) -> NoteKind:
    if value in NOTE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_KIND_VALUES!r}")
