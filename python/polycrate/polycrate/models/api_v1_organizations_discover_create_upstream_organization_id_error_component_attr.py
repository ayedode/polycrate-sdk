from typing import Literal

ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponentAttr = Literal["upstream_organization_id"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponentAttr
] = {
    "upstream_organization_id",
}


def check_api_v1_organizations_discover_create_upstream_organization_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateUpstreamOrganizationIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
