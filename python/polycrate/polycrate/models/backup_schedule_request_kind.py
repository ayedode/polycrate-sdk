from typing import Literal

BackupScheduleRequestKind = Literal["app", "cluster", "database"]

BACKUP_SCHEDULE_REQUEST_KIND_VALUES: set[BackupScheduleRequestKind] = {
    "app",
    "cluster",
    "database",
}


def check_backup_schedule_request_kind(value: str) -> BackupScheduleRequestKind:
    if value in BACKUP_SCHEDULE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_REQUEST_KIND_VALUES!r}")
