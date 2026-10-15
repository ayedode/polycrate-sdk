from typing import Literal

NoteListKind = Literal[
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

NOTE_LIST_KIND_VALUES: set[NoteListKind] = {
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


def check_note_list_kind(value: str) -> NoteListKind:
    if value in NOTE_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_LIST_KIND_VALUES!r}")
