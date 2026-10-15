from typing import Literal

BackupListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

BACKUP_LIST_STATE_VALUES: set[BackupListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_backup_list_state(value: str) -> BackupListState:
    if value in BACKUP_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_LIST_STATE_VALUES!r}")
