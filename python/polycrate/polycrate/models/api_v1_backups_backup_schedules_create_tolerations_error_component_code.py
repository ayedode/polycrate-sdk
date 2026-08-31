from typing import Literal

ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backup_schedules_create_tolerations_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateTolerationsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
