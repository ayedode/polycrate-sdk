from typing import Literal

BackupScheduleScope = Literal["system", "user"]

BACKUP_SCHEDULE_SCOPE_VALUES: set[BackupScheduleScope] = {
    "system",
    "user",
}


def check_backup_schedule_scope(value: str) -> BackupScheduleScope:
    if value in BACKUP_SCHEDULE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_SCOPE_VALUES!r}")
