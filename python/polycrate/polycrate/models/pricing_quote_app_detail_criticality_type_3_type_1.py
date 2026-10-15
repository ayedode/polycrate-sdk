from typing import Literal

PricingQuoteAppDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PRICING_QUOTE_APP_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PricingQuoteAppDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_quote_app_detail_criticality_type_3_type_1(value: str) -> PricingQuoteAppDetailCriticalityType3Type1:
    if value in PRICING_QUOTE_APP_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
