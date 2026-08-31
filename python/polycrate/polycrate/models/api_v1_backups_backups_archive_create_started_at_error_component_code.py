from typing import Literal

ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backups_archive_create_started_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateStartedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
