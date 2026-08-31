from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_backups_backup_schedules_partial_update_status_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateStatusErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
