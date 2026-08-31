from typing import Literal

ApiV1BackupsBackupSchedulesUpdatePausedErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_PAUSED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdatePausedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backup_schedules_update_paused_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdatePausedErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_PAUSED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_PAUSED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
