from typing import Literal

PricingQuoteSimpleState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_SIMPLE_STATE_VALUES: set[PricingQuoteSimpleState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_simple_state(value: str) -> PricingQuoteSimpleState:
    if value in PRICING_QUOTE_SIMPLE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_SIMPLE_STATE_VALUES!r}")
