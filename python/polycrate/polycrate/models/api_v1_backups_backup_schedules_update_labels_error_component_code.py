from typing import Literal

ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_backups_backup_schedules_update_labels_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateLabelsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
