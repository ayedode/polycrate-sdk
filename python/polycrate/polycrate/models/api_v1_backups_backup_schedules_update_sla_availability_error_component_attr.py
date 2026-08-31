from typing import Literal

ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_backups_backup_schedules_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
