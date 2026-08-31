from typing import Literal

ApiV1CvesArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_CVES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_cves_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1CvesArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_CVES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
