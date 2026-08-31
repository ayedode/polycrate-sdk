from typing import Literal

ApiV1AlertroutersArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_ALERTROUTERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1AlertroutersArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_alertrouters_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1AlertroutersArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_ALERTROUTERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
