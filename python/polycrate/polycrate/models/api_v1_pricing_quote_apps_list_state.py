from typing import Literal

ApiV1PricingQuoteAppsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_QUOTE_APPS_LIST_STATE_VALUES: set[ApiV1PricingQuoteAppsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_quote_apps_list_state(value: str) -> ApiV1PricingQuoteAppsListState:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_STATE_VALUES!r}")
