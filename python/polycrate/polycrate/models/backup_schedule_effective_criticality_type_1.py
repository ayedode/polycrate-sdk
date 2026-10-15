from typing import Literal

BackupScheduleEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BACKUP_SCHEDULE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BackupScheduleEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_backup_schedule_effective_criticality_type_1(value: str) -> BackupScheduleEffectiveCriticalityType1:
    if value in BACKUP_SCHEDULE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
