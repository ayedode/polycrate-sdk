from typing import Literal

ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_LAST_BACKUP_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backup_schedules_update_last_backup_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateLastBackupAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_LAST_BACKUP_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_LAST_BACKUP_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
