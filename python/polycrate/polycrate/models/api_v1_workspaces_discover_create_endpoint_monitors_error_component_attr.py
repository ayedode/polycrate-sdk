from typing import Literal

ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponentAttr = Literal["endpoint_monitors"]

API_V1_WORKSPACES_DISCOVER_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponentAttr
] = {
    "endpoint_monitors",
}


def check_api_v1_workspaces_discover_create_endpoint_monitors_error_component_attr(
    value: str,
) -> ApiV1WorkspacesDiscoverCreateEndpointMonitorsErrorComponentAttr:
    if value in API_V1_WORKSPACES_DISCOVER_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_DISCOVER_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
