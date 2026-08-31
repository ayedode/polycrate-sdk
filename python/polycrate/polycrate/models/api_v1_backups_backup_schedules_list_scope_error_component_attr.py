from typing import Literal

ApiV1BackupsBackupSchedulesListScopeErrorComponentAttr = Literal["scope"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_backups_backup_schedules_list_scope_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListScopeErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
