from typing import Literal

PricingQuoteDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_DETAIL_LAST_STATE_VALUES: set[PricingQuoteDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_detail_last_state(value: str) -> PricingQuoteDetailLastState:
    if value in PRICING_QUOTE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_DETAIL_LAST_STATE_VALUES!r}")
