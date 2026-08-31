from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponentAttr = Literal["total_backups"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponentAttr
] = {
    "total_backups",
}


def check_api_v1_backups_backup_schedules_archive_create_total_backups_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateTotalBackupsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_TOTAL_BACKUPS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
