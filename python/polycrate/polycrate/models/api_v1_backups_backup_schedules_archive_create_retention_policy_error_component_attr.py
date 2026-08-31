from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponentAttr = Literal["retention_policy"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponentAttr
] = {
    "retention_policy",
}


def check_api_v1_backups_backup_schedules_archive_create_retention_policy_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateRetentionPolicyErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
