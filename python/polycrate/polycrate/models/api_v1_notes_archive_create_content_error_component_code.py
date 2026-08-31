from typing import Literal

ApiV1NotesArchiveCreateContentErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1_NOTES_ARCHIVE_CREATE_CONTENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesArchiveCreateContentErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_notes_archive_create_content_error_component_code(
    value: str,
) -> ApiV1NotesArchiveCreateContentErrorComponentCode:
    if value in API_V1_NOTES_ARCHIVE_CREATE_CONTENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_CONTENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
