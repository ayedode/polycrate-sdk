from typing import Literal

BackupScheduleRequestStatus = Literal["active", "failed", "paused", "unknown"]

BACKUP_SCHEDULE_REQUEST_STATUS_VALUES: set[BackupScheduleRequestStatus] = {
    "active",
    "failed",
    "paused",
    "unknown",
}


def check_backup_schedule_request_status(value: str) -> BackupScheduleRequestStatus:
    if value in BACKUP_SCHEDULE_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_REQUEST_STATUS_VALUES!r}")
