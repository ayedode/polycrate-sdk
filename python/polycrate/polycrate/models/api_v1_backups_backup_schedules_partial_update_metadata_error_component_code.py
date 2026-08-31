from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backup_schedules_partial_update_metadata_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateMetadataErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
