from typing import Literal

ApiV1BackupsBackupSchedulesListProvider = Literal["cloudnativepg", "custom", "velero"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_PROVIDER_VALUES: set[ApiV1BackupsBackupSchedulesListProvider] = {
    "cloudnativepg",
    "custom",
    "velero",
}


def check_api_v1_backups_backup_schedules_list_provider(value: str) -> ApiV1BackupsBackupSchedulesListProvider:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_PROVIDER_VALUES!r}"
    )
