from typing import Literal

ApiV1NotesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_NOTES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesUpdateLabelsErrorComponentCode] = {
    "invalid",
}


def check_api_v1_notes_update_labels_error_component_code(value: str) -> ApiV1NotesUpdateLabelsErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
