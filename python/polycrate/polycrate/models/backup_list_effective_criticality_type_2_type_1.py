from typing import Literal

BackupListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

BACKUP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[BackupListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_backup_list_effective_criticality_type_2_type_1(value: str) -> BackupListEffectiveCriticalityType2Type1:
    if value in BACKUP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {BACKUP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
