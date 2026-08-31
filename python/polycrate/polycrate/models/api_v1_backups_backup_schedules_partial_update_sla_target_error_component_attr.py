from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_backups_backup_schedules_partial_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
