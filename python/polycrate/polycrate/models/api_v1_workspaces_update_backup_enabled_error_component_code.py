from typing import Literal

ApiV1WorkspacesUpdateBackupEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateBackupEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_backup_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateBackupEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_UPDATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
