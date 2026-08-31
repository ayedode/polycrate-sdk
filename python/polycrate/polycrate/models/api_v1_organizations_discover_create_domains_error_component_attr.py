from typing import Literal

ApiV1OrganizationsDiscoverCreateDomainsErrorComponentAttr = Literal["domains"]

API_V1_ORGANIZATIONS_DISCOVER_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsDiscoverCreateDomainsErrorComponentAttr
] = {
    "domains",
}


def check_api_v1_organizations_discover_create_domains_error_component_attr(
    value: str,
) -> ApiV1OrganizationsDiscoverCreateDomainsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_DISCOVER_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_DISCOVER_CREATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
