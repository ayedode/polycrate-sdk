from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponentAttr = Literal["import_domains"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponentAttr
] = {
    "import_domains",
}


def check_api_v1_domains_domain_registrars_partial_update_import_domains_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateImportDomainsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
