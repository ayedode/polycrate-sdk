from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_API_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domain_registrars_update_api_credential_id_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateApiCredentialIdErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_API_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_API_CREDENTIAL_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
