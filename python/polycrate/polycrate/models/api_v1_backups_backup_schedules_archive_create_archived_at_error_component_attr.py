from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_backups_backup_schedules_archive_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
