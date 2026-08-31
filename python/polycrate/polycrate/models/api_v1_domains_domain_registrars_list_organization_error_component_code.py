from typing import Literal

ApiV1DomainsDomainRegistrarsListOrganizationErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsListOrganizationErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_domains_domain_registrars_list_organization_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsListOrganizationErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_LIST_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
