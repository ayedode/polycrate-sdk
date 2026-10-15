from typing import Literal

NoteSimpleKind = Literal[
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

NOTE_SIMPLE_KIND_VALUES: set[NoteSimpleKind] = {
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


def check_note_simple_kind(value: str) -> NoteSimpleKind:
    if value in NOTE_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_SIMPLE_KIND_VALUES!r}")
