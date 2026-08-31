from typing import Literal

ApiV1BackupsBackupSchedulesListKind = Literal["app", "cluster", "database"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_VALUES: set[ApiV1BackupsBackupSchedulesListKind] = {
    "app",
    "cluster",
    "database",
}


def check_api_v1_backups_backup_schedules_list_kind(value: str) -> ApiV1BackupsBackupSchedulesListKind:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_VALUES!r}")
