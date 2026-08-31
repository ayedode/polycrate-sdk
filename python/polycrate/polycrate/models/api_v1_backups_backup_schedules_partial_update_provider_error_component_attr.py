from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_backups_backup_schedules_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
