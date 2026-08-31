from typing import Literal

ApiV1PricingQuoteAppsListKind = Literal["generic"]

API_V1_PRICING_QUOTE_APPS_LIST_KIND_VALUES: set[ApiV1PricingQuoteAppsListKind] = {
    "generic",
}


def check_api_v1_pricing_quote_apps_list_kind(value: str) -> ApiV1PricingQuoteAppsListKind:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_KIND_VALUES!r}")
