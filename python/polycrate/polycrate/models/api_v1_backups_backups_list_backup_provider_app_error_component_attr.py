from typing import Literal

ApiV1BackupsBackupsListBackupProviderAppErrorComponentAttr = Literal["backup_provider_app"]

API_V1_BACKUPS_BACKUPS_LIST_BACKUP_PROVIDER_APP_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListBackupProviderAppErrorComponentAttr
] = {
    "backup_provider_app",
}


def check_api_v1_backups_backups_list_backup_provider_app_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListBackupProviderAppErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_BACKUP_PROVIDER_APP_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_BACKUP_PROVIDER_APP_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
