from typing import Literal

BackupRequestProvider = Literal["cloudnativepg", "custom", "velero"]

BACKUP_REQUEST_PROVIDER_VALUES: set[BackupRequestProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_backup_request_provider(value: str) -> BackupRequestProvider:
    if value in BACKUP_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_REQUEST_PROVIDER_VALUES!r}")
