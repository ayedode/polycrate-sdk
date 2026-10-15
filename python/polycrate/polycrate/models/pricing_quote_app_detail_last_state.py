from typing import Literal

PricingQuoteAppDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_APP_DETAIL_LAST_STATE_VALUES: set[PricingQuoteAppDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_app_detail_last_state(value: str) -> PricingQuoteAppDetailLastState:
    if value in PRICING_QUOTE_APP_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_LAST_STATE_VALUES!r}")
