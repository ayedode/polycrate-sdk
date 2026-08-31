from typing import Literal

ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_backups_backup_schedules_create_total_backups_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
