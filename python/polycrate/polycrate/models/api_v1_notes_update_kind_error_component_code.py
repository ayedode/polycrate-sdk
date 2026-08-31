from typing import Literal

ApiV1NotesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesUpdateKindErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notes_update_kind_error_component_code(value: str) -> ApiV1NotesUpdateKindErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
