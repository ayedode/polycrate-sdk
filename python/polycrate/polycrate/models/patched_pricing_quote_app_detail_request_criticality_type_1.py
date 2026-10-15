from typing import Literal

PatchedPricingQuoteAppDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_PRICING_QUOTE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PatchedPricingQuoteAppDetailRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pricing_quote_app_detail_request_criticality_type_1(
    value: str,
) -> PatchedPricingQuoteAppDetailRequestCriticalityType1:
    if value in PATCHED_PRICING_QUOTE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_QUOTE_APP_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
