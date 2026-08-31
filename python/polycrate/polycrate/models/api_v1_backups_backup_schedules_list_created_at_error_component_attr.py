from typing import Literal

ApiV1BackupsBackupSchedulesListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_backups_backup_schedules_list_created_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListCreatedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
