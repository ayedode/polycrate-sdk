from typing import Literal

ApiV1PricingQuoteAppsCreateCountErrorComponentAttr = Literal["count"]

API_V1_PRICING_QUOTE_APPS_CREATE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateCountErrorComponentAttr
] = {
    "count",
}


def check_api_v1_pricing_quote_apps_create_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
