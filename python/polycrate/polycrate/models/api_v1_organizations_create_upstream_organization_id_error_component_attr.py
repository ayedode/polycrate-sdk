from typing import Literal

ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponentAttr = Literal["upstream_organization_id"]

API_V1_ORGANIZATIONS_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponentAttr
] = {
    "upstream_organization_id",
}


def check_api_v1_organizations_create_upstream_organization_id_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateUpstreamOrganizationIdErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_UPSTREAM_ORGANIZATION_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
