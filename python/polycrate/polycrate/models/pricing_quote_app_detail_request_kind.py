from typing import Literal

PricingQuoteAppDetailRequestKind = Literal["generic"]

PRICING_QUOTE_APP_DETAIL_REQUEST_KIND_VALUES: set[PricingQuoteAppDetailRequestKind] = {
    "generic",
}


def check_pricing_quote_app_detail_request_kind(value: str) -> PricingQuoteAppDetailRequestKind:
    if value in PRICING_QUOTE_APP_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_REQUEST_KIND_VALUES!r}")
