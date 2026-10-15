from typing import Literal

BackupListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

BACKUP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[BackupListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_backup_list_effective_criticality_type_1(value: str) -> BackupListEffectiveCriticalityType1:
    if value in BACKUP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
