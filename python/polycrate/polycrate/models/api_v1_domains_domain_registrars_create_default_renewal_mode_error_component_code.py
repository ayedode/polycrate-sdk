from typing import Literal

ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_domains_domain_registrars_create_default_renewal_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
