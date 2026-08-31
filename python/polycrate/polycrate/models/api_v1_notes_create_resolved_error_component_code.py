from typing import Literal

ApiV1NotesCreateResolvedErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_CREATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateResolvedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_notes_create_resolved_error_component_code(value: str) -> ApiV1NotesCreateResolvedErrorComponentCode:
    if value in API_V1_NOTES_CREATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
