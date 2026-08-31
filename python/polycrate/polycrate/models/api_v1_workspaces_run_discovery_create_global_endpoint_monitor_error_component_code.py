from typing import Literal

ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_run_discovery_create_global_endpoint_monitor_error_component_code(
    value: str,
) -> ApiV1WorkspacesRunDiscoveryCreateGlobalEndpointMonitorErrorComponentCode:
    if value in API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RUN_DISCOVERY_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
