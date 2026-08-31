from typing import Literal

BackupScheduleStatusEnum = Literal["active", "failed", "paused", "unknown"]

BACKUP_SCHEDULE_STATUS_ENUM_VALUES: set[BackupScheduleStatusEnum] = {
    "active",
    "failed",
    "paused",
    "unknown",
}


def check_backup_schedule_status_enum(value: str) -> BackupScheduleStatusEnum:
    if value in BACKUP_SCHEDULE_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_STATUS_ENUM_VALUES!r}")
