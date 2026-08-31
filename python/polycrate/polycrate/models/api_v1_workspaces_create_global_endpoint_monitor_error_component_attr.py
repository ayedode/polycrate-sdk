from typing import Literal

ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponentAttr = Literal["global_endpoint_monitor"]

API_V1_WORKSPACES_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponentAttr
] = {
    "global_endpoint_monitor",
}


def check_api_v1_workspaces_create_global_endpoint_monitor_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateGlobalEndpointMonitorErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_GLOBAL_ENDPOINT_MONITOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
