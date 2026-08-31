from typing import Literal

ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_backups_backup_schedules_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
