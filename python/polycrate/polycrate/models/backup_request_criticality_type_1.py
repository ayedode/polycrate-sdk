from typing import Literal

BackupRequestCriticalityType1 = Literal["", "high", "low", "medium"]

BACKUP_REQUEST_CRITICALITY_TYPE_1_VALUES: set[BackupRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_backup_request_criticality_type_1(value: str) -> BackupRequestCriticalityType1:
    if value in BACKUP_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
