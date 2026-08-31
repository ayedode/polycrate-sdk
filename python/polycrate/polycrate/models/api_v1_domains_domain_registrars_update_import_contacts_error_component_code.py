from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_CONTACTS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domain_registrars_update_import_contacts_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_CONTACTS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_CONTACTS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
