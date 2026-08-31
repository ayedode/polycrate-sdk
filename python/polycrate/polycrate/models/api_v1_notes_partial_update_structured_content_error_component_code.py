from typing import Literal

ApiV1NotesPartialUpdateStructuredContentErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_PARTIAL_UPDATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesPartialUpdateStructuredContentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_partial_update_structured_content_error_component_code(
    value: str,
) -> ApiV1NotesPartialUpdateStructuredContentErrorComponentCode:
    if value in API_V1_NOTES_PARTIAL_UPDATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_PARTIAL_UPDATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
