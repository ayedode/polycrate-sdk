from typing import Literal

BackupLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BACKUP_LAST_STATE_VALUES: set[BackupLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_backup_last_state(value: str) -> BackupLastState:
    if value in BACKUP_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_LAST_STATE_VALUES!r}")
