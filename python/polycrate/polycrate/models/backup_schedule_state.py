from typing import Literal

BackupScheduleState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BACKUP_SCHEDULE_STATE_VALUES: set[BackupScheduleState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_backup_schedule_state(value: str) -> BackupScheduleState:
    if value in BACKUP_SCHEDULE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_STATE_VALUES!r}")
