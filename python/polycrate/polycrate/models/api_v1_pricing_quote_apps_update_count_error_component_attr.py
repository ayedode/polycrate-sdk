from typing import Literal

ApiV1PricingQuoteAppsUpdateCountErrorComponentAttr = Literal["count"]

API_V1_PRICING_QUOTE_APPS_UPDATE_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateCountErrorComponentAttr
] = {
    "count",
}


def check_api_v1_pricing_quote_apps_update_count_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateCountErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
