from typing import Literal

ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponentAttr = Literal["quoted_price"]

API_V1_PRICING_QUOTE_APPS_CREATE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponentAttr
] = {
    "quoted_price",
}


def check_api_v1_pricing_quote_apps_create_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
