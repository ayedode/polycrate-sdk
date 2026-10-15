from typing import Literal

PatchedBackupRequestKind = Literal["app", "cluster", "database"]

PATCHED_BACKUP_REQUEST_KIND_VALUES: set[PatchedBackupRequestKind] = {
    "app",
    "cluster",
    "database",
}


def check_patched_backup_request_kind(value: str) -> PatchedBackupRequestKind:
    if value in PATCHED_BACKUP_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_REQUEST_KIND_VALUES!r}")
