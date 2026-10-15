from typing import Literal

BackupScheduleStatus = Literal["active", "failed", "paused", "unknown"]

BACKUP_SCHEDULE_STATUS_VALUES: set[BackupScheduleStatus] = {
    "active",
    "failed",
    "paused",
    "unknown",
}


def check_backup_schedule_status(value: str) -> BackupScheduleStatus:
    if value in BACKUP_SCHEDULE_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_STATUS_VALUES!r}")
