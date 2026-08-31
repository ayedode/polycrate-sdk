from typing import Literal

ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponentAttr = Literal["endpoint_monitors"]

API_V1_WORKSPACES_CHECK_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponentAttr
] = {
    "endpoint_monitors",
}


def check_api_v1_workspaces_check_create_endpoint_monitors_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateEndpointMonitorsErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
