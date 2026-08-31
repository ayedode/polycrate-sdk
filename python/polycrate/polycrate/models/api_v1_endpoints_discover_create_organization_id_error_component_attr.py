from typing import Literal

ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponentAttr = Literal["organization_id"]

API_V1_ENDPOINTS_DISCOVER_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponentAttr
] = {
    "organization_id",
}


def check_api_v1_endpoints_discover_create_organization_id_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateOrganizationIdErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
