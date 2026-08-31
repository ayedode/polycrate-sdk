from typing import Literal

ApiV1WorkspacesCheckCreateBackupEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CHECK_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateBackupEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_check_create_backup_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateBackupEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
