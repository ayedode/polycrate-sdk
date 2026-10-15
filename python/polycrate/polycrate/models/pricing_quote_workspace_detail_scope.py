from typing import Literal

PricingQuoteWorkspaceDetailScope = Literal["system", "user"]

PRICING_QUOTE_WORKSPACE_DETAIL_SCOPE_VALUES: set[PricingQuoteWorkspaceDetailScope] = {
    "system",
    "user",
}


def check_pricing_quote_workspace_detail_scope(value: str) -> PricingQuoteWorkspaceDetailScope:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_SCOPE_VALUES!r}")
