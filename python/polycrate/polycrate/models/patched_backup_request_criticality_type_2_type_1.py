from typing import Literal

PatchedBackupRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_BACKUP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedBackupRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_backup_request_criticality_type_2_type_1(value: str) -> PatchedBackupRequestCriticalityType2Type1:
    if value in PATCHED_BACKUP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
