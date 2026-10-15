from typing import Literal

PricingQuoteDetailKind = Literal["generic"]

PRICING_QUOTE_DETAIL_KIND_VALUES: set[PricingQuoteDetailKind] = {
    "generic",
}


def check_pricing_quote_detail_kind(value: str) -> PricingQuoteDetailKind:
    if value in PRICING_QUOTE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_DETAIL_KIND_VALUES!r}")
