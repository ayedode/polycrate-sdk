from typing import Literal

PatchedBackupScheduleRequestProvider = Literal["cloudnativepg", "custom", "velero"]

PATCHED_BACKUP_SCHEDULE_REQUEST_PROVIDER_VALUES: set[PatchedBackupScheduleRequestProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_patched_backup_schedule_request_provider(value: str) -> PatchedBackupScheduleRequestProvider:
    if value in PATCHED_BACKUP_SCHEDULE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_SCHEDULE_REQUEST_PROVIDER_VALUES!r}")
