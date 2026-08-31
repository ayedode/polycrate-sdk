from typing import Literal

ApiV1BackupsBackupSchedulesListStatusErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListStatusErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backup_schedules_list_status_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListStatusErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
