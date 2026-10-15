from typing import Literal

PricingQuoteAppDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_APP_DETAIL_STATE_VALUES: set[PricingQuoteAppDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_app_detail_state(value: str) -> PricingQuoteAppDetailState:
    if value in PRICING_QUOTE_APP_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_STATE_VALUES!r}")
