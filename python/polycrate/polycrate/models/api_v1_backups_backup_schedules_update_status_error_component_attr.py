from typing import Literal

ApiV1BackupsBackupSchedulesUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_backups_backup_schedules_update_status_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateStatusErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
