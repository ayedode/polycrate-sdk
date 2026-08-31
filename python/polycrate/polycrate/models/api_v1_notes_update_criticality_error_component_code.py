from typing import Literal

ApiV1NotesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_NOTES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesUpdateCriticalityErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_notes_update_criticality_error_component_code(
    value: str,
) -> ApiV1NotesUpdateCriticalityErrorComponentCode:
    if value in API_V1_NOTES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
