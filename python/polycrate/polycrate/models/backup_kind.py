from typing import Literal

BackupKind = Literal["app", "cluster", "database"]

BACKUP_KIND_VALUES: set[BackupKind] = {
    "app",
    "cluster",
    "database",
}


def check_backup_kind(value: str) -> BackupKind:
    if value in BACKUP_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_KIND_VALUES!r}")
