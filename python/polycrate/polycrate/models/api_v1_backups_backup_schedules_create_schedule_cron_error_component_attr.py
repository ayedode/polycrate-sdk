from typing import Literal

ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponentAttr = Literal["schedule_cron"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_SCHEDULE_CRON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponentAttr
] = {
    "schedule_cron",
}


def check_api_v1_backups_backup_schedules_create_schedule_cron_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateScheduleCronErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_SCHEDULE_CRON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_SCHEDULE_CRON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
