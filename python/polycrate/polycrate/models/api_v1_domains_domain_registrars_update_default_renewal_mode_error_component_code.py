from typing import Literal

ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domain_registrars_update_default_renewal_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsUpdateDefaultRenewalModeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_UPDATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
