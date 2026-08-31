from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_global_endpoint_monitor_error_component_code(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateGlobalEndpointMonitorErrorComponentCode:
    if (
        value
        in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
