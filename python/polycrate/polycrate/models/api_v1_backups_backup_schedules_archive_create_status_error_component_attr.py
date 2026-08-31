from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponentAttr = Literal["status"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_backups_backup_schedules_archive_create_status_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateStatusErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
