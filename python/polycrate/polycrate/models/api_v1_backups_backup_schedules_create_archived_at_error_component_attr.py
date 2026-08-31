from typing import Literal

ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_backups_backup_schedules_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateArchivedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
