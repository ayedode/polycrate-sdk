from typing import Literal

PricingQuoteWorkspaceDetailRequestKind = Literal["generic"]

PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_KIND_VALUES: set[PricingQuoteWorkspaceDetailRequestKind] = {
    "generic",
}


def check_pricing_quote_workspace_detail_request_kind(value: str) -> PricingQuoteWorkspaceDetailRequestKind:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_KIND_VALUES!r}"
    )
