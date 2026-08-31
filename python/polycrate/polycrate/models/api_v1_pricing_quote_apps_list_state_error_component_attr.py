from typing import Literal

ApiV1PricingQuoteAppsListStateErrorComponentAttr = Literal["state"]

API_V1_PRICING_QUOTE_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_pricing_quote_apps_list_state_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsListStateErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
