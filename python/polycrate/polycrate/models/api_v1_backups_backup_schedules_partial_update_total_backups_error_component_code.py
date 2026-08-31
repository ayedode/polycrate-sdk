from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOTAL_BACKUPS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_backups_backup_schedules_partial_update_total_backups_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOTAL_BACKUPS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOTAL_BACKUPS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
