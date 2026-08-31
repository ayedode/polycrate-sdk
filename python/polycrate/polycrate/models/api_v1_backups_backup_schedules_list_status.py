from typing import Literal

ApiV1BackupsBackupSchedulesListStatus = Literal["active", "failed", "paused", "unknown"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_VALUES: set[ApiV1BackupsBackupSchedulesListStatus] = {
    "active",
    "failed",
    "paused",
    "unknown",
}


def check_api_v1_backups_backup_schedules_list_status(value: str) -> ApiV1BackupsBackupSchedulesListStatus:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATUS_VALUES!r}"
    )
