from typing import Literal

ApiV1PricingQuotesCreateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_QUOTES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuotesCreateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_quotes_create_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuotesCreateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
