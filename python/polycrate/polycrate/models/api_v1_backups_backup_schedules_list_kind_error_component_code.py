from typing import Literal

ApiV1BackupsBackupSchedulesListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backup_schedules_list_kind_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesListKindErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
