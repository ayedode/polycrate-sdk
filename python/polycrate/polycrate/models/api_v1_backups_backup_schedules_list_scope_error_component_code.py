from typing import Literal

ApiV1BackupsBackupSchedulesListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backup_schedules_list_scope_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListScopeErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
