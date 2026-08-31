from typing import Literal

ApiV1PricingQuotesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_QUOTES_LIST_STATE_VALUES: set[ApiV1PricingQuotesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_quotes_list_state(value: str) -> ApiV1PricingQuotesListState:
    if value in API_V1_PRICING_QUOTES_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTES_LIST_STATE_VALUES!r}")
