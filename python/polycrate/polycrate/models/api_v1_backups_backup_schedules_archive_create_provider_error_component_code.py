from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_backups_backup_schedules_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateProviderErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
