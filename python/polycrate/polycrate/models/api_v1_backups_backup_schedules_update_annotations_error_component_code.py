from typing import Literal

ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_backups_backup_schedules_update_annotations_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateAnnotationsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
