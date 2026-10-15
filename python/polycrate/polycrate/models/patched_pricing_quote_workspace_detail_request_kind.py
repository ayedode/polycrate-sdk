from typing import Literal

PatchedPricingQuoteWorkspaceDetailRequestKind = Literal["generic"]

PATCHED_PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_KIND_VALUES: set[PatchedPricingQuoteWorkspaceDetailRequestKind] = {
    "generic",
}


def check_patched_pricing_quote_workspace_detail_request_kind(
    value: str,
) -> PatchedPricingQuoteWorkspaceDetailRequestKind:
    if value in PATCHED_PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_QUOTE_WORKSPACE_DETAIL_REQUEST_KIND_VALUES!r}"
    )
