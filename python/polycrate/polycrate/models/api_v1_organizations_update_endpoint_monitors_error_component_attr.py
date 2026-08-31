from typing import Literal

ApiV1OrganizationsUpdateEndpointMonitorsErrorComponentAttr = Literal["endpoint_monitors"]

API_V1_ORGANIZATIONS_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsUpdateEndpointMonitorsErrorComponentAttr
] = {
    "endpoint_monitors",
}


def check_api_v1_organizations_update_endpoint_monitors_error_component_attr(
    value: str,
) -> ApiV1OrganizationsUpdateEndpointMonitorsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
