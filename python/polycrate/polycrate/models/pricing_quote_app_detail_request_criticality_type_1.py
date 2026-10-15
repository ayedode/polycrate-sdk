from typing import Literal

PricingQuoteAppDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PRICING_QUOTE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PricingQuoteAppDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_quote_app_detail_request_criticality_type_1(
    value: str,
) -> PricingQuoteAppDetailRequestCriticalityType1:
    if value in PRICING_QUOTE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
