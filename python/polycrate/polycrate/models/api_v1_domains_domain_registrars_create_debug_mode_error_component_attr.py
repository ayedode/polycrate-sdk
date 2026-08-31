from typing import Literal

ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_domains_domain_registrars_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainRegistrarsCreateDebugModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAIN_REGISTRARS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
