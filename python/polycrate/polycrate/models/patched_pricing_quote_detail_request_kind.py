from typing import Literal

PatchedPricingQuoteDetailRequestKind = Literal["generic"]

PATCHED_PRICING_QUOTE_DETAIL_REQUEST_KIND_VALUES: set[PatchedPricingQuoteDetailRequestKind] = {
    "generic",
}


def check_patched_pricing_quote_detail_request_kind(value: str) -> PatchedPricingQuoteDetailRequestKind:
    if value in PATCHED_PRICING_QUOTE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_QUOTE_DETAIL_REQUEST_KIND_VALUES!r}")
