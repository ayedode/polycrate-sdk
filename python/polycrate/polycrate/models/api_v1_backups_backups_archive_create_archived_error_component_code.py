from typing import Literal

ApiV1BackupsBackupsArchiveCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_archive_create_archived_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateArchivedErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
