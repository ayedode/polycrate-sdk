from typing import Literal

ApiV1PricingQuotesCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_QUOTES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_quotes_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
