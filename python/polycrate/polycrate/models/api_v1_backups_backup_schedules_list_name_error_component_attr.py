from typing import Literal

ApiV1BackupsBackupSchedulesListNameErrorComponentAttr = Literal["name"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_backups_backup_schedules_list_name_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListNameErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
