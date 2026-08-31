from typing import Literal

ApiV1BackupsBackupSchedulesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_backups_backup_schedules_create_provider_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateProviderErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
