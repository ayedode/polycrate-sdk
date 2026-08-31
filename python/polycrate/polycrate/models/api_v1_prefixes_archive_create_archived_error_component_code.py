from typing import Literal

ApiV1PrefixesArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PREFIXES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PrefixesArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_prefixes_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1PrefixesArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_PREFIXES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
