from typing import Literal

ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_quote_apps_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
