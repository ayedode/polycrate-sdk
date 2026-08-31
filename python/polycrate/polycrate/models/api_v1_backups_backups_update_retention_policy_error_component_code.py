from typing import Literal

ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BACKUPS_BACKUPS_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_backups_backups_update_retention_policy_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateRetentionPolicyErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_RETENTION_POLICY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
