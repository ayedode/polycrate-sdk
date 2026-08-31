from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_backups_backup_schedules_archive_create_labels_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateLabelsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
