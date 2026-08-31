from typing import Literal

ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponentAttr = Literal[
    "endpoint_monitoring_mode"
]

API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponentAttr
] = {
    "endpoint_monitoring_mode",
}


def check_api_v1_workspaces_update_workspace_poly_partial_update_endpoint_monitoring_mode_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateWorkspacePolyPartialUpdateEndpointMonitoringModeErrorComponentAttr:
    if (
        value
        in API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES
    ):
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_WORKSPACE_POLY_PARTIAL_UPDATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
