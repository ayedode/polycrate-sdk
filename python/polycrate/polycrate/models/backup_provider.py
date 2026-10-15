from typing import Literal

BackupProvider = Literal["cloudnativepg", "custom", "velero"]

BACKUP_PROVIDER_VALUES: set[BackupProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_backup_provider(value: str) -> BackupProvider:
    if value in BACKUP_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_PROVIDER_VALUES!r}")
