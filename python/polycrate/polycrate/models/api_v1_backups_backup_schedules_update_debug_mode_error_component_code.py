from typing import Literal

ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backup_schedules_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateDebugModeErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
