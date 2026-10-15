from typing import Literal

PricingQuoteAppListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_APP_LIST_STATE_VALUES: set[PricingQuoteAppListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_app_list_state(value: str) -> PricingQuoteAppListState:
    if value in PRICING_QUOTE_APP_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_LIST_STATE_VALUES!r}")
