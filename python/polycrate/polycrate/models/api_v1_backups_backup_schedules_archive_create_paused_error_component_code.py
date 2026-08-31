from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PAUSED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backup_schedules_archive_create_paused_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreatePausedErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PAUSED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PAUSED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
