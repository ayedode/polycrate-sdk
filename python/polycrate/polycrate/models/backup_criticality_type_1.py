from typing import Literal

BackupCriticalityType1 = Literal["", "high", "low", "medium"]

BACKUP_CRITICALITY_TYPE_1_VALUES: set[BackupCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_backup_criticality_type_1(value: str) -> BackupCriticalityType1:
    if value in BACKUP_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_CRITICALITY_TYPE_1_VALUES!r}")
