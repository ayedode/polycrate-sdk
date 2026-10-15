from typing import Literal

PricingQuoteAppDetailKind = Literal["generic"]

PRICING_QUOTE_APP_DETAIL_KIND_VALUES: set[PricingQuoteAppDetailKind] = {
    "generic",
}


def check_pricing_quote_app_detail_kind(value: str) -> PricingQuoteAppDetailKind:
    if value in PRICING_QUOTE_APP_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_KIND_VALUES!r}")
