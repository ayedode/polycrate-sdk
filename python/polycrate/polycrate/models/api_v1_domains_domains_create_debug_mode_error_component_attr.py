from typing import Literal

ApiV1DomainsDomainsCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_DOMAINS_DOMAINS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDomainsCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_domains_domains_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDomainsCreateDebugModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DOMAINS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
