from typing import Literal

PatchedPricingQuoteAppDetailRequestKind = Literal["generic"]

PATCHED_PRICING_QUOTE_APP_DETAIL_REQUEST_KIND_VALUES: set[PatchedPricingQuoteAppDetailRequestKind] = {
    "generic",
}


def check_patched_pricing_quote_app_detail_request_kind(value: str) -> PatchedPricingQuoteAppDetailRequestKind:
    if value in PATCHED_PRICING_QUOTE_APP_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_QUOTE_APP_DETAIL_REQUEST_KIND_VALUES!r}"
    )
