from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_SCHEDULE_CRON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_backups_backup_schedules_archive_create_schedule_cron_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateScheduleCronErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_SCHEDULE_CRON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_SCHEDULE_CRON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
