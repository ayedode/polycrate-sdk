from typing import Literal

ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_backups_backup_schedules_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
