from typing import Literal

ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_backups_backup_schedules_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
