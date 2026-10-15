from typing import Literal

BackupScheduleKind = Literal["app", "cluster", "database"]

BACKUP_SCHEDULE_KIND_VALUES: set[BackupScheduleKind] = {
    "app",
    "cluster",
    "database",
}


def check_backup_schedule_kind(value: str) -> BackupScheduleKind:
    if value in BACKUP_SCHEDULE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_KIND_VALUES!r}")
