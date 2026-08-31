from typing import Literal

ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domain_registrars_create_import_domains_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
