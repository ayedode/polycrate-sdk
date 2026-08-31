from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponentAttr = Literal["total_backups"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponentAttr
] = {
    "total_backups",
}


def check_api_v1_backups_backup_schedules_partial_update_total_backups_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateTotalBackupsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
