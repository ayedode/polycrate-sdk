from typing import Literal

ApiV1BackupsBackupSchedulesListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_VALUES: set[ApiV1BackupsBackupSchedulesListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1_backups_backup_schedules_list_time_range(value: str) -> ApiV1BackupsBackupSchedulesListTimeRange:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_VALUES!r}"
    )
