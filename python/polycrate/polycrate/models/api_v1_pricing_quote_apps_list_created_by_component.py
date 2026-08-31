from typing import Literal

ApiV1PricingQuoteAppsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_QUOTE_APPS_LIST_CREATED_BY_COMPONENT_VALUES: set[ApiV1PricingQuoteAppsListCreatedByComponent] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_quote_apps_list_created_by_component(
    value: str,
) -> ApiV1PricingQuoteAppsListCreatedByComponent:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
