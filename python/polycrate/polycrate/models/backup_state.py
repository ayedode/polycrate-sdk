from typing import Literal

BackupState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BACKUP_STATE_VALUES: set[BackupState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_backup_state(value: str) -> BackupState:
    if value in BACKUP_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_STATE_VALUES!r}")
