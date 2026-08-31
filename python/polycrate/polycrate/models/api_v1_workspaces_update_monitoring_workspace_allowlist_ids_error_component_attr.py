from typing import Literal

ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponentAttr = Literal["monitoring_workspace_allowlist_ids"]

API_V1_WORKSPACES_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponentAttr
] = {
    "monitoring_workspace_allowlist_ids",
}


def check_api_v1_workspaces_update_monitoring_workspace_allowlist_ids_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateMonitoringWorkspaceAllowlistIdsErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_MONITORING_WORKSPACE_ALLOWLIST_IDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
