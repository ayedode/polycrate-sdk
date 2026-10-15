from typing import Literal

PricingQuoteDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_DETAIL_STATE_VALUES: set[PricingQuoteDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_detail_state(value: str) -> PricingQuoteDetailState:
    if value in PRICING_QUOTE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_DETAIL_STATE_VALUES!r}")
