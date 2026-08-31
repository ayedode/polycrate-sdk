from typing import Literal

ApiV1PricingQuoteAppsListKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTE_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_quote_apps_list_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsListKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
