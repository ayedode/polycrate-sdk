from typing import Literal

BackupScheduleLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BACKUP_SCHEDULE_LAST_STATE_VALUES: set[BackupScheduleLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_backup_schedule_last_state(value: str) -> BackupScheduleLastState:
    if value in BACKUP_SCHEDULE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_LAST_STATE_VALUES!r}")
