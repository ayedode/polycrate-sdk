from typing import Literal

ApiV1NotesCreateStructuredContentErrorComponentCode = Literal["invalid", "null"]

API_V1_NOTES_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesCreateStructuredContentErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_notes_create_structured_content_error_component_code(
    value: str,
) -> ApiV1NotesCreateStructuredContentErrorComponentCode:
    if value in API_V1_NOTES_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_STRUCTURED_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
