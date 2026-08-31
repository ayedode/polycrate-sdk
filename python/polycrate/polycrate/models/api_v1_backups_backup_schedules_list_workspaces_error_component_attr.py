from typing import Literal

ApiV1BackupsBackupSchedulesListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_backups_backup_schedules_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListWorkspacesErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
