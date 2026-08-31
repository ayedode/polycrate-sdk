from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponentAttr = Literal["paused"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PAUSED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponentAttr
] = {
    "paused",
}


def check_api_v1_backups_backup_schedules_partial_update_paused_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdatePausedErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PAUSED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PAUSED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
