from typing import Literal

ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backup_schedules_create_criticality_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateCriticalityErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
