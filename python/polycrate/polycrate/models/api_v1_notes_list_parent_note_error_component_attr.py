from typing import Literal

ApiV1NotesListParentNoteErrorComponentAttr = Literal["parent_note"]

API_V1_NOTES_LIST_PARENT_NOTE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesListParentNoteErrorComponentAttr] = {
    "parent_note",
}


def check_api_v1_notes_list_parent_note_error_component_attr(value: str) -> ApiV1NotesListParentNoteErrorComponentAttr:
    if value in API_V1_NOTES_LIST_PARENT_NOTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_LIST_PARENT_NOTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
