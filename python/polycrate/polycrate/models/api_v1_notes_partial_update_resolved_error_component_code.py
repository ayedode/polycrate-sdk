from typing import Literal

ApiV1NotesPartialUpdateResolvedErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_PARTIAL_UPDATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateResolvedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_partial_update_resolved_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateResolvedErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_RESOLVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
