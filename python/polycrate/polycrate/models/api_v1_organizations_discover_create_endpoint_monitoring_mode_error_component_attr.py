from typing import Literal

ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponentAttr = Literal["endpoint_monitoring_mode"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponentAttr
] = {
    "endpoint_monitoring_mode",
}


def check_api_v1_organizations_discover_create_endpoint_monitoring_mode_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateEndpointMonitoringModeErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
