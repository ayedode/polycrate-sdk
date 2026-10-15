from typing import Literal

BackupRequestStatus = Literal["completed", "expired", "failed", "partial", "pending", "running", "unknown"]

BACKUP_REQUEST_STATUS_VALUES: set[BackupRequestStatus] = {
    "completed",
    "expired",
    "failed",
    "partial",
    "pending",
    "running",
    "unknown",
}


def check_backup_request_status(value: str) -> BackupRequestStatus:
    if value in BACKUP_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_REQUEST_STATUS_VALUES!r}")
