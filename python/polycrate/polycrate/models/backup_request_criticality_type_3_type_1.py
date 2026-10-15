from typing import Literal

BackupRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

BACKUP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[BackupRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_backup_request_criticality_type_3_type_1(value: str) -> BackupRequestCriticalityType3Type1:
    if value in BACKUP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
