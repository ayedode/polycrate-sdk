from typing import Literal

ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_domains_domain_registrars_list_organizations_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListOrganizationsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
