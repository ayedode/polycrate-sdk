from typing import Literal

ApiV1PricingQuoteAppsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_PRICING_QUOTE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_pricing_quote_apps_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsListUpdatedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
