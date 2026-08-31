from typing import Literal

ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponentAttr = Literal["import_domains"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponentAttr
] = {
    "import_domains",
}


def check_api_v1_domains_domain_registrars_archive_create_import_domains_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsArchiveCreateImportDomainsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_ARCHIVE_CREATE_IMPORT_DOMAINS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
