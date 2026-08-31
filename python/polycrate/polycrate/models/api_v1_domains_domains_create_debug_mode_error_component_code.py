from typing import Literal

ApiV1DomainsDomainsCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_DOMAINS_DOMAINS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_domains_domains_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsCreateDebugModeErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
