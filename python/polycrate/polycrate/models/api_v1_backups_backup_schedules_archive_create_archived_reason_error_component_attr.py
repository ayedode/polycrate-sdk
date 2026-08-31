from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_backups_backup_schedules_archive_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
