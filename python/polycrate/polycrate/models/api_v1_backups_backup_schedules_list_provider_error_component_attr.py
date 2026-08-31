from typing import Literal

ApiV1BackupsBackupSchedulesListProviderErrorComponentAttr = Literal["provider"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_backups_backup_schedules_list_provider_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListProviderErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
