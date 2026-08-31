from typing import Literal

ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponentAttr = Literal["import_contacts"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_CONTACTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponentAttr
] = {
    "import_contacts",
}


def check_api_v1_domains_domain_registrars_create_import_contacts_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_CONTACTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_CONTACTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
