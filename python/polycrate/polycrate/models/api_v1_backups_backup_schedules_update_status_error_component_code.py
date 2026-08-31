from typing import Literal

ApiV1BackupsBackupSchedulesUpdateStatusErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateStatusErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_backups_backup_schedules_update_status_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateStatusErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
