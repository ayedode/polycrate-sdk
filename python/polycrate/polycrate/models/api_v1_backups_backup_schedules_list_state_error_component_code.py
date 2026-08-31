from typing import Literal

ApiV1BackupsBackupSchedulesListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backup_schedules_list_state_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListStateErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
