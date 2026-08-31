from typing import Literal

ApiV1BackupsBackupSchedulesListNameExactErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListNameExactErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_backups_backup_schedules_list_name_exact_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListNameExactErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_NAME_EXACT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
