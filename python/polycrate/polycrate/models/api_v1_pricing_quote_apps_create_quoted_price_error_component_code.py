from typing import Literal

ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_QUOTE_APPS_CREATE_QUOTED_PRICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_quote_apps_create_quoted_price_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_QUOTED_PRICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_QUOTED_PRICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
