from typing import Literal

BackupKindEnum = Literal["app", "cluster", "database"]

BACKUP_KIND_ENUM_VALUES: set[BackupKindEnum] = {
    "app",
    "cluster",
    "database",
}


def check_backup_kind_enum(value: str) -> BackupKindEnum:
    if value in BACKUP_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_KIND_ENUM_VALUES!r}")
