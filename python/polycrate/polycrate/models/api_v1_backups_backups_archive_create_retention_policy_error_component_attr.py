from typing import Literal

ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponentAttr = Literal["retention_policy"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponentAttr
] = {
    "retention_policy",
}


def check_api_v1_backups_backups_archive_create_retention_policy_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateRetentionPolicyErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
