from typing import Literal

NoteRequestKind = Literal[
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

NOTE_REQUEST_KIND_VALUES: set[NoteRequestKind] = {
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


def check_note_request_kind(value: str) -> NoteRequestKind:
    if value in NOTE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_REQUEST_KIND_VALUES!r}")
