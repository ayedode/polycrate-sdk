from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponentAttr = Literal["import_domains"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponentAttr
] = {
    "import_domains",
}


def check_api_v1_domains_domain_registrars_update_import_domains_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateImportDomainsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
