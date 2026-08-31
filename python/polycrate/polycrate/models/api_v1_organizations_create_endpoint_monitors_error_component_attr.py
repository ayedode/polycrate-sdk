from typing import Literal

ApiV1OrganizationsCreateEndpointMonitorsErrorComponentAttr = Literal["endpoint_monitors"]

API_V1_ORGANIZATIONS_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateEndpointMonitorsErrorComponentAttr
] = {
    "endpoint_monitors",
}


def check_api_v1_organizations_create_endpoint_monitors_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateEndpointMonitorsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
