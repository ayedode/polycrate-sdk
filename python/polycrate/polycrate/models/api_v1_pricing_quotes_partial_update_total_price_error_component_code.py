from typing import Literal

ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_QUOTES_PARTIAL_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_quotes_partial_update_total_price_error_component_code(
    value: str,
) -> ApiV1PricingQuotesPartialUpdateTotalPriceErrorComponentCode:
    if value in API_V1_PRICING_QUOTES_PARTIAL_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_PARTIAL_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
