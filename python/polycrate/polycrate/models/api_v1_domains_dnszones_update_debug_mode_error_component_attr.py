from typing import Literal

ApiV1DomainsDnszonesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_DOMAINS_DNSZONES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DomainsDnszonesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_domains_dnszones_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1DomainsDnszonesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_DOMAINS_DNSZONES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DNSZONES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
