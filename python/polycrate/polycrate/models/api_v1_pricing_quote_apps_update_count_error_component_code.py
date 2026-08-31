from typing import Literal

ApiV1PricingQuoteAppsUpdateCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_PRICING_QUOTE_APPS_UPDATE_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsUpdateCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_pricing_quote_apps_update_count_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateCountErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
