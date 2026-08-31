from typing import Literal

ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponentAttr = Literal["default_renewal_mode"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponentAttr
] = {
    "default_renewal_mode",
}


def check_api_v1_domains_domain_registrars_create_default_renewal_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateDefaultRenewalModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
