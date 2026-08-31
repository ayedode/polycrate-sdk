from typing import Literal

ApiV1BackupsBackupSchedulesListScope = Literal["system", "user"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_VALUES: set[ApiV1BackupsBackupSchedulesListScope] = {
    "system",
    "user",
}


def check_api_v1_backups_backup_schedules_list_scope(value: str) -> ApiV1BackupsBackupSchedulesListScope:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SCOPE_VALUES!r}"
    )
