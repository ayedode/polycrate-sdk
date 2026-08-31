from typing import Literal

NoteKindEnum = Literal[
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

NOTE_KIND_ENUM_VALUES: set[NoteKindEnum] = {
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


def check_note_kind_enum(value: str) -> NoteKindEnum:
    if value in NOTE_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTE_KIND_ENUM_VALUES!r}")
