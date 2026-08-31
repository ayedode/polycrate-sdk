from typing import Literal

ApiV1BackupsBackupsListBackupProviderAppErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_BACKUPS_BACKUPS_LIST_BACKUP_PROVIDER_APP_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsListBackupProviderAppErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_backups_backups_list_backup_provider_app_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsListBackupProviderAppErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_LIST_BACKUP_PROVIDER_APP_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_BACKUP_PROVIDER_APP_ERROR_COMPONENT_CODE_VALUES!r}"
    )
