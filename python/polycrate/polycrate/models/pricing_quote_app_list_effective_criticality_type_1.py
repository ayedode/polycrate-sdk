from typing import Literal

PricingQuoteAppListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PRICING_QUOTE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[PricingQuoteAppListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_pricing_quote_app_list_effective_criticality_type_1(
    value: str,
) -> PricingQuoteAppListEffectiveCriticalityType1:
    if value in PRICING_QUOTE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_APP_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
