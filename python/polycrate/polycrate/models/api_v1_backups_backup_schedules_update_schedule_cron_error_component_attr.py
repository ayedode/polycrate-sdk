from typing import Literal

ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponentAttr = Literal["schedule_cron"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SCHEDULE_CRON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponentAttr
] = {
    "schedule_cron",
}


def check_api_v1_backups_backup_schedules_update_schedule_cron_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateScheduleCronErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SCHEDULE_CRON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SCHEDULE_CRON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
