from typing import Literal

BackupScheduleListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BACKUP_SCHEDULE_LIST_STATE_VALUES: set[BackupScheduleListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_backup_schedule_list_state(value: str) -> BackupScheduleListState:
    if value in BACKUP_SCHEDULE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_LIST_STATE_VALUES!r}")
