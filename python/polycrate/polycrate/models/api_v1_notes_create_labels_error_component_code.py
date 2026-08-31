from typing import Literal

ApiV1NotesCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_NOTES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_notes_create_labels_error_component_code(value: str) -> ApiV1NotesCreateLabelsErrorComponentCode:
    if value in API_V1_NOTES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
