from typing import Literal

ApiV1BackupsBackupSchedulesListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_backups_backup_schedules_list_created_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListCreatedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
