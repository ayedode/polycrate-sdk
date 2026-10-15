from typing import Literal

PricingQuoteDetailRequestKind = Literal["generic"]

PRICING_QUOTE_DETAIL_REQUEST_KIND_VALUES: set[PricingQuoteDetailRequestKind] = {
    "generic",
}


def check_pricing_quote_detail_request_kind(value: str) -> PricingQuoteDetailRequestKind:
    if value in PRICING_QUOTE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_DETAIL_REQUEST_KIND_VALUES!r}")
