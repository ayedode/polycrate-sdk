from typing import Literal

ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponentAttr = Literal["retention_policy"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponentAttr
] = {
    "retention_policy",
}


def check_api_v1_backups_backups_partial_update_retention_policy_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateRetentionPolicyErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
