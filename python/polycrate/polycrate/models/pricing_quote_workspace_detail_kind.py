from typing import Literal

PricingQuoteWorkspaceDetailKind = Literal["generic"]

PRICING_QUOTE_WORKSPACE_DETAIL_KIND_VALUES: set[PricingQuoteWorkspaceDetailKind] = {
    "generic",
}


def check_pricing_quote_workspace_detail_kind(value: str) -> PricingQuoteWorkspaceDetailKind:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_KIND_VALUES!r}")
