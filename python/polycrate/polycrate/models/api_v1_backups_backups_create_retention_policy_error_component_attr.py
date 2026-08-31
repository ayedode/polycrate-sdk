from typing import Literal

ApiV1BackupsBackupsCreateRetentionPolicyErrorComponentAttr = Literal["retention_policy"]

API_V1_BACKUPS_BACKUPS_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateRetentionPolicyErrorComponentAttr
] = {
    "retention_policy",
}


def check_api_v1_backups_backups_create_retention_policy_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateRetentionPolicyErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
