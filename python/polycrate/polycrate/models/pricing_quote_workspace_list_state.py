from typing import Literal

PricingQuoteWorkspaceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_QUOTE_WORKSPACE_LIST_STATE_VALUES: set[PricingQuoteWorkspaceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_quote_workspace_list_state(value: str) -> PricingQuoteWorkspaceListState:
    if value in PRICING_QUOTE_WORKSPACE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_LIST_STATE_VALUES!r}")
