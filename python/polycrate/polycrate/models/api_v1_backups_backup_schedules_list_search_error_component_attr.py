from typing import Literal

ApiV1BackupsBackupSchedulesListSearchErrorComponentAttr = Literal["search"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListSearchErrorComponentAttr
] = {
    "search",
}


def check_api_v1_backups_backup_schedules_list_search_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListSearchErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
