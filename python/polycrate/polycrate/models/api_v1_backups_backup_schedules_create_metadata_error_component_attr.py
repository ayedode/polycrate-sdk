from typing import Literal

ApiV1BackupsBackupSchedulesCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_backups_backup_schedules_create_metadata_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateMetadataErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
