from typing import Literal

ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponentAttr = Literal["import_domains"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponentAttr
] = {
    "import_domains",
}


def check_api_v1_domains_domain_registrars_create_import_domains_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateImportDomainsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
