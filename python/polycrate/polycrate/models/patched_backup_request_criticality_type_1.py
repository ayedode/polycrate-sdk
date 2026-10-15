from typing import Literal

PatchedBackupRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_BACKUP_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedBackupRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_backup_request_criticality_type_1(value: str) -> PatchedBackupRequestCriticalityType1:
    if value in PATCHED_BACKUP_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
