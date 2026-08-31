from typing import Literal

ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponentAttr = Literal["retention_policy"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponentAttr
] = {
    "retention_policy",
}


def check_api_v1_backups_backup_schedules_update_retention_policy_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateRetentionPolicyErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
