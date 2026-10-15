from typing import Literal

PricingQuoteWorkspaceDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_WORKSPACE_DETAIL_LAST_STATE_VALUES: set[PricingQuoteWorkspaceDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_workspace_detail_last_state(value: str) -> PricingQuoteWorkspaceDetailLastState:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_LAST_STATE_VALUES!r}")
