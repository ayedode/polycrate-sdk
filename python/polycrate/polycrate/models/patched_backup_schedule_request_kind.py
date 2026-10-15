from typing import Literal

PatchedBackupScheduleRequestKind = Literal["app", "cluster", "database"]

PATCHED_BACKUP_SCHEDULE_REQUEST_KIND_VALUES: set[PatchedBackupScheduleRequestKind] = {
    "app",
    "cluster",
    "database",
}


def check_patched_backup_schedule_request_kind(value: str) -> PatchedBackupScheduleRequestKind:
    if value in PATCHED_BACKUP_SCHEDULE_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_SCHEDULE_REQUEST_KIND_VALUES!r}")
