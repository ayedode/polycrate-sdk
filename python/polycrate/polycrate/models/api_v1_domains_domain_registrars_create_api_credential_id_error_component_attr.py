from typing import Literal

ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponentAttr = Literal["api_credential_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponentAttr
] = {
    "api_credential_id",
}


def check_api_v1_domains_domain_registrars_create_api_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateApiCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
