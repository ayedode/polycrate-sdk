from typing import Literal

ApiV1BackupsBackupSchedulesCreatePausedErrorComponentAttr = Literal["paused"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PAUSED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreatePausedErrorComponentAttr
] = {
    "paused",
}


def check_api_v1_backups_backup_schedules_create_paused_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreatePausedErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PAUSED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PAUSED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
