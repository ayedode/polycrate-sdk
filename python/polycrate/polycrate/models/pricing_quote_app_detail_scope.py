from typing import Literal

PricingQuoteAppDetailScope = Literal["system", "user"]

PRICING_QUOTE_APP_DETAIL_SCOPE_VALUES: set[PricingQuoteAppDetailScope] = {
    "system",
    "user",
}


def check_pricing_quote_app_detail_scope(value: str) -> PricingQuoteAppDetailScope:
    if value in PRICING_QUOTE_APP_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_SCOPE_VALUES!r}")
