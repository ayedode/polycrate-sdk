from typing import Literal

ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponentAttr = Literal["last_backup_at"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_LAST_BACKUP_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponentAttr
] = {
    "last_backup_at",
}


def check_api_v1_backups_backup_schedules_create_last_backup_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateLastBackupAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_LAST_BACKUP_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_LAST_BACKUP_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
