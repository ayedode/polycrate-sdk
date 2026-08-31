from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_backups_backup_schedules_partial_update_metadata_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
