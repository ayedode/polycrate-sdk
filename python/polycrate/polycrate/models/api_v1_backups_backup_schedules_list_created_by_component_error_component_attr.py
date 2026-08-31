from typing import Literal

ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1_backups_backup_schedules_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListCreatedByComponentErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
