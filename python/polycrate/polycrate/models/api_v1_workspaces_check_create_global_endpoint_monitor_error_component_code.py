from typing import Literal

ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_CHECK_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_check_create_global_endpoint_monitor_error_component_code(
    value: str,
) -> ApiV1WorkspacesCheckCreateGlobalEndpointMonitorErrorComponentCode:
    if value in API_V1_WORKSPACES_CHECK_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_CODE_VALUES!r}"
    )
