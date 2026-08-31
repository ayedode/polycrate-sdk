from typing import Literal

ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_backups_backup_schedules_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateSlaTargetErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
