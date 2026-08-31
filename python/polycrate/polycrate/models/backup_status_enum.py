from typing import Literal

BackupStatusEnum = Literal["completed", "expired", "failed", "partial", "pending", "running", "unknown"]

BACKUP_STATUS_ENUM_VALUES: set[BackupStatusEnum] = {
    "completed",
    "expired",
    "failed",
    "partial",
    "pending",
    "running",
    "unknown",
}


def check_backup_status_enum(value: str) -> BackupStatusEnum:
    if value in BACKUP_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_STATUS_ENUM_VALUES!r}")
