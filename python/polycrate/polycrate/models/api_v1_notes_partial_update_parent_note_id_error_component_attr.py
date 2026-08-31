from typing import Literal

ApiV1NotesPartialUpdateParentNoteIdErrorComponentAttr = Literal["parent_note_id"]

API_V1_NOTES_PARTIAL_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesPartialUpdateParentNoteIdErrorComponentAttr
] = {
    "parent_note_id",
}


def check_api_v1_notes_partial_update_parent_note_id_error_component_attr(
    value: str,
) -> ApiV1NotesPartialUpdateParentNoteIdErrorComponentAttr:
    if value in API_V1_NOTES_PARTIAL_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
