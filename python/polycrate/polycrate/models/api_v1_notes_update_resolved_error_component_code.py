from typing import Literal

ApiV1NotesUpdateResolvedErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_UPDATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesUpdateResolvedErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_notes_update_resolved_error_component_code(value: str) -> ApiV1NotesUpdateResolvedErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
