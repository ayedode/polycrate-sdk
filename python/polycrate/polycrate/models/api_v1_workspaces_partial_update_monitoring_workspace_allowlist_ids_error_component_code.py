from typing import Literal

ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_WORKSPACES_PARTIAL_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_workspaces_partial_update_monitoring_workspace_allowlist_ids_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateMonitoringWorkspaceAllowlistIdsErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
