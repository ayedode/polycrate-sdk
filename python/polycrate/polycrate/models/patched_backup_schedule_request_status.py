from typing import Literal

PatchedBackupScheduleRequestStatus = Literal["active", "failed", "paused", "unknown"]

PATCHED_BACKUP_SCHEDULE_REQUEST_STATUS_VALUES: set[PatchedBackupScheduleRequestStatus] = {
    "active",
    "failed",
    "paused",
    "unknown",
}


def check_patched_backup_schedule_request_status(value: str) -> PatchedBackupScheduleRequestStatus:
    if value in PATCHED_BACKUP_SCHEDULE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_SCHEDULE_REQUEST_STATUS_VALUES!r}")
