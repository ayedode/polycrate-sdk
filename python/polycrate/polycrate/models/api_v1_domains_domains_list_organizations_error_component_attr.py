from typing import Literal

ApiV1DomainsDomainsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_DOMAINS_DOMAINS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_domains_domains_list_organizations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsListOrganizationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
