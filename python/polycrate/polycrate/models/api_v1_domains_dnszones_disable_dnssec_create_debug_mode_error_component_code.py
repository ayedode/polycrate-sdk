from typing import Literal

ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnszones_disable_dnssec_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDnszonesDisableDnssecCreateDebugModeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_DISABLE_DNSSEC_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
