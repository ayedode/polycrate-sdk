from typing import Literal

PricingQuoteAppListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PRICING_QUOTE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PricingQuoteAppListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_pricing_quote_app_list_effective_criticality_type_2_type_1(
    value: str,
) -> PricingQuoteAppListEffectiveCriticalityType2Type1:
    if value in PRICING_QUOTE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
