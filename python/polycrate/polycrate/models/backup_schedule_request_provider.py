from typing import Literal

BackupScheduleRequestProvider = Literal["cloudnativepg", "custom", "velero"]

BACKUP_SCHEDULE_REQUEST_PROVIDER_VALUES: set[BackupScheduleRequestProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_backup_schedule_request_provider(value: str) -> BackupScheduleRequestProvider:
    if value in BACKUP_SCHEDULE_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_REQUEST_PROVIDER_VALUES!r}")
