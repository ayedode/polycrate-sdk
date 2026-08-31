from typing import Literal

ApiV1BackupsBackupSchedulesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATE_VALUES: set[ApiV1BackupsBackupSchedulesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_backups_backup_schedules_list_state(value: str) -> ApiV1BackupsBackupSchedulesListState:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_STATE_VALUES!r}"
    )
