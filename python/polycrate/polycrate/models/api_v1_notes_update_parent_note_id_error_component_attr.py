from typing import Literal

ApiV1NotesUpdateParentNoteIdErrorComponentAttr = Literal["parent_note_id"]

API_V1_NOTES_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1NotesUpdateParentNoteIdErrorComponentAttr] = {
    "parent_note_id",
}


def check_api_v1_notes_update_parent_note_id_error_component_attr(
    value: str,
) -> ApiV1NotesUpdateParentNoteIdErrorComponentAttr:
    if value in API_V1_NOTES_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
