from typing import Literal

BackupScheduleCriticalityType1 = Literal["", "high", "low", "medium"]

BACKUP_SCHEDULE_CRITICALITY_TYPE_1_VALUES: set[BackupScheduleCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_backup_schedule_criticality_type_1(value: str) -> BackupScheduleCriticalityType1:
    if value in BACKUP_SCHEDULE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_CRITICALITY_TYPE_1_VALUES!r}")
