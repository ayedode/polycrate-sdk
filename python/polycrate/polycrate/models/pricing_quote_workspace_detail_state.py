from typing import Literal

PricingQuoteWorkspaceDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_WORKSPACE_DETAIL_STATE_VALUES: set[PricingQuoteWorkspaceDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_workspace_detail_state(value: str) -> PricingQuoteWorkspaceDetailState:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_STATE_VALUES!r}")
