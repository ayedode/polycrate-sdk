from typing import Literal

PatchedBackupRequestProvider = Literal["cloudnativepg", "custom", "velero"]

PATCHED_BACKUP_REQUEST_PROVIDER_VALUES: set[PatchedBackupRequestProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_patched_backup_request_provider(value: str) -> PatchedBackupRequestProvider:
    if value in PATCHED_BACKUP_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_BACKUP_REQUEST_PROVIDER_VALUES!r}")
