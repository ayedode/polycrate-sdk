from typing import Literal

BackupScheduleProvider = Literal["cloudnativepg", "custom", "velero"]

BACKUP_SCHEDULE_PROVIDER_VALUES: set[BackupScheduleProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_backup_schedule_provider(value: str) -> BackupScheduleProvider:
    if value in BACKUP_SCHEDULE_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_SCHEDULE_PROVIDER_VALUES!r}")
