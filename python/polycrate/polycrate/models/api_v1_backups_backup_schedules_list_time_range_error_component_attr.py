from typing import Literal

ApiV1BackupsBackupSchedulesListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_backups_backup_schedules_list_time_range_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesListTimeRangeErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
