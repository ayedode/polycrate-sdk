from typing import Literal

BackupStatus = Literal["completed", "expired", "failed", "partial", "pending", "running", "unknown"]

BACKUP_STATUS_VALUES: set[BackupStatus] = {
    "completed",
    "expired",
    "failed",
    "partial",
    "pending",
    "running",
    "unknown",
}


def check_backup_status(value: str) -> BackupStatus:
    if value in BACKUP_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_STATUS_VALUES!r}")
