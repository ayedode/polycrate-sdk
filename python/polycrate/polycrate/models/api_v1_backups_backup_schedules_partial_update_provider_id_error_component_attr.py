from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_backups_backup_schedules_partial_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateProviderIdErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
