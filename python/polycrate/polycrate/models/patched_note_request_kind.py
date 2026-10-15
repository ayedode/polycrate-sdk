from typing import Literal

PatchedNoteRequestKind = Literal[
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

PATCHED_NOTE_REQUEST_KIND_VALUES: set[PatchedNoteRequestKind] = {
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


def check_patched_note_request_kind(value: str) -> PatchedNoteRequestKind:
    if value in PATCHED_NOTE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_NOTE_REQUEST_KIND_VALUES!r}")
