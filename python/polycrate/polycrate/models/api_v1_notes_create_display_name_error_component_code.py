from typing import Literal

ApiV1NotesCreateDisplayNameErrorComponentCode = Literal[
    "blank", "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_NOTES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1NotesCreateDisplayNameErrorComponentCode] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_notes_create_display_name_error_component_code(
    value: str,
) -> ApiV1NotesCreateDisplayNameErrorComponentCode:
    if value in API_V1_NOTES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_CREATE_DISPLAY_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
