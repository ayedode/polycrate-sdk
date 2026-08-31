from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponentAttr = Literal["api_credential_id"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponentAttr
] = {
    "api_credential_id",
}


def check_api_v1_domains_domain_registrars_update_api_credential_id_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_API_CREDENTIAL_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
