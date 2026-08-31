from typing import Literal

ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_backups_backup_schedules_update_sla_target_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateSlaTargetErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
