from typing import Literal

ApiV1DomainsDomainRegistrarsListOrganizationErrorComponentAttr = Literal["organization"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsListOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_domains_domain_registrars_list_organization_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListOrganizationErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
