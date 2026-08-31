from typing import Literal

ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_CONTACTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domain_registrars_create_import_contacts_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateImportContactsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_CONTACTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_IMPORT_CONTACTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
