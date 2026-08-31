from typing import Literal

ApiV1NotesArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_NOTES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1NotesArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_notes_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1NotesArchiveCreateProviderErrorComponentCode:
    if value in API_V1_NOTES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
