from typing import Literal

BackupCriticalityType2Type1 = Literal["", "high", "low", "medium"]

BACKUP_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[BackupCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_backup_criticality_type_2_type_1(value: str) -> BackupCriticalityType2Type1:
    if value in BACKUP_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
