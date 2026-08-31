from typing import Literal

ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponentAttr = Literal["default_renewal_mode"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponentAttr
] = {
    "default_renewal_mode",
}


def check_api_v1_domains_domain_registrars_partial_update_default_renewal_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsPartialUpdateDefaultRenewalModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_PARTIAL_UPDATE_DEFAULT_RENEWAL_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
