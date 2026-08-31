from typing import Literal

BackupProviderEnum = Literal["cloudnativepg", "custom", "velero"]

BACKUP_PROVIDER_ENUM_VALUES: set[BackupProviderEnum] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_backup_provider_enum(value: str) -> BackupProviderEnum:
    if value in BACKUP_PROVIDER_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BACKUP_PROVIDER_ENUM_VALUES!r}")
