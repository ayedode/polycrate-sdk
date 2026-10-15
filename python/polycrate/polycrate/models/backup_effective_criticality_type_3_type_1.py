from typing import Literal

BackupEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

BACKUP_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[BackupEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_backup_effective_criticality_type_3_type_1(value: str) -> BackupEffectiveCriticalityType3Type1:
    if value in BACKUP_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BACKUP_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
