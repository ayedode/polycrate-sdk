from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_backup_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateBackupEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
