from typing import Literal

PricingQuoteDetailScope = Literal["system", "user"]

PRICING_QUOTE_DETAIL_SCOPE_VALUES: set[PricingQuoteDetailScope] = {
    "system",
    "user",
}


def check_pricing_quote_detail_scope(value: str) -> PricingQuoteDetailScope:
    if value in PRICING_QUOTE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_DETAIL_SCOPE_VALUES!r}")
