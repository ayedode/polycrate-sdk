from typing import Literal

ApiV1BackupsBackupSchedulesListStatusErrorComponentAttr = Literal["status"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_backups_backup_schedules_list_status_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListStatusErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
