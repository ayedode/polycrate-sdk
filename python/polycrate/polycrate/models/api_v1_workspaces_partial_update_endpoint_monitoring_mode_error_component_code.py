from typing import Literal

ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_PARTIAL_UPDATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_partial_update_endpoint_monitoring_mode_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateEndpointMonitoringModeErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
