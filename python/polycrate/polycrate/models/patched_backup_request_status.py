from typing import Literal

PatchedBackupRequestStatus = Literal["completed", "expired", "failed", "partial", "pending", "running", "unknown"]

PATCHED_BACKUP_REQUEST_STATUS_VALUES: set[PatchedBackupRequestStatus] = {
    "completed",
    "expired",
    "failed",
    "partial",
    "pending",
    "running",
    "unknown",
}


def check_patched_backup_request_status(value: str) -> PatchedBackupRequestStatus:
    if value in PATCHED_BACKUP_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_REQUEST_STATUS_VALUES!r}")
