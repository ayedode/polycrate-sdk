from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponentAttr = Literal["last_backup_at"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_LAST_BACKUP_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponentAttr
] = {
    "last_backup_at",
}


def check_api_v1_backups_backup_schedules_partial_update_last_backup_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateLastBackupAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_LAST_BACKUP_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_LAST_BACKUP_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
