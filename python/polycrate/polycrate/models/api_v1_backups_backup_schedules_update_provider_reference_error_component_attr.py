from typing import Literal

ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_backups_backup_schedules_update_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateProviderReferenceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
