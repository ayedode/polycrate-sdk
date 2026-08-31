from typing import Literal

ApiV1NotesPartialUpdateParentNoteIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_NOTES_PARTIAL_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateParentNoteIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_notes_partial_update_parent_note_id_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateParentNoteIdErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_PARENT_NOTE_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
