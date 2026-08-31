from typing import Literal

ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_monitoring_workspace_allowlist_ids_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateMonitoringWorkspaceAllowlistIdsErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
