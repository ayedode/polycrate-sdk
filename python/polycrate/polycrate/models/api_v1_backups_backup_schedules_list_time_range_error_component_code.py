from typing import Literal

ApiV1BackupsBackupSchedulesListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backup_schedules_list_time_range_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListTimeRangeErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
