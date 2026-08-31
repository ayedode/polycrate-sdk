from typing import Literal

ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backup_schedules_update_archived_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateArchivedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
