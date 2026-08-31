from typing import Literal

ApiV1DomainsDnsrecordsCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DNSRECORDS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDnsrecordsCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_dnsrecords_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDnsrecordsCreateDebugModeErrorComponentCode:
    if value in API_V1_DOMAINS_DNSRECORDS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSRECORDS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
