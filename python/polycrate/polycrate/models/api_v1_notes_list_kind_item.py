from typing import Literal

ApiV1NotesListKindItem = Literal[
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

API_V1_NOTES_LIST_KIND_ITEM_VALUES: set[ApiV1NotesListKindItem] = {
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


def check_api_v1_notes_list_kind_item(value: str) -> ApiV1NotesListKindItem:
    if value in API_V1_NOTES_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_KIND_ITEM_VALUES!r}")
