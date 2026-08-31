from typing import Literal

ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_domains_dnszones_refresh_dnssec_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesRefreshDnssecCreateDebugModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_REFRESH_DNSSEC_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
