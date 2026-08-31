from typing import Literal

ApiV1OrganizationsPartialUpdateDomainsErrorComponentAttr = Literal["domains"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateDomainsErrorComponentAttr
] = {
    "domains",
}


def check_api_v1_organizations_partial_update_domains_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateDomainsErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
