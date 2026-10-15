from typing import Literal

BackupScope = Literal["system", "user"]

BACKUP_SCOPE_VALUES: set[BackupScope] = {
    "system",
    "user",
}


def check_backup_scope(value: str) -> BackupScope:
    if value in BACKUP_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCOPE_VALUES!r}")
