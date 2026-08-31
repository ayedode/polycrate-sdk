from typing import Literal

ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_WORKSPACES_RECONCILE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_workspaces_reconcile_create_endpoint_monitoring_mode_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreateEndpointMonitoringModeErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
