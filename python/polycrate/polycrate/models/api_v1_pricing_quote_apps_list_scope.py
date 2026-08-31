from typing import Literal

ApiV1PricingQuoteAppsListScope = Literal["system", "user"]

API_V1_PRICING_QUOTE_APPS_LIST_SCOPE_VALUES: set[ApiV1PricingQuoteAppsListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_quote_apps_list_scope(value: str) -> ApiV1PricingQuoteAppsListScope:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_SCOPE_VALUES!r}")
