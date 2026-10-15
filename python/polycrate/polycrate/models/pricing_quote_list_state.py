from typing import Literal

PricingQuoteListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_LIST_STATE_VALUES: set[PricingQuoteListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_list_state(value: str) -> PricingQuoteListState:
    if value in PRICING_QUOTE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_LIST_STATE_VALUES!r}")
