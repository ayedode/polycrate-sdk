from typing import Literal

PatchedBackupScheduleRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_BACKUP_SCHEDULE_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedBackupScheduleRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_backup_schedule_request_criticality_type_1(
    value: str,
) -> PatchedBackupScheduleRequestCriticalityType1:
    if value in PATCHED_BACKUP_SCHEDULE_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_SCHEDULE_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
