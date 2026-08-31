from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponentAttr = Literal["import_contacts"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_CONTACTS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponentAttr
] = {
    "import_contacts",
}


def check_api_v1_domains_domain_registrars_update_import_contacts_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateImportContactsErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_CONTACTS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_IMPORT_CONTACTS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
