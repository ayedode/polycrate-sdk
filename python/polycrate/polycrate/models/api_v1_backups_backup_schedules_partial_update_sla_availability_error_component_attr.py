from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_backups_backup_schedules_partial_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
