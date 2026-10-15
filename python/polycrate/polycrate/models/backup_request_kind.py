from typing import Literal

BackupRequestKind = Literal["app", "cluster", "database"]

BACKUP_REQUEST_KIND_VALUES: set[BackupRequestKind] = {
    "app",
    "cluster",
    "database",
}


def check_backup_request_kind(value: str) -> BackupRequestKind:
    if value in BACKUP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_REQUEST_KIND_VALUES!r}")
