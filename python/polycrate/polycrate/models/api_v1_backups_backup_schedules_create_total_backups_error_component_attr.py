from typing import Literal

ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponentAttr = Literal["total_backups"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponentAttr
] = {
    "total_backups",
}


def check_api_v1_backups_backup_schedules_create_total_backups_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateTotalBackupsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
