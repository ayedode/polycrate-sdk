from typing import Literal

PricingQuoteWorkspaceDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PRICING_QUOTE_WORKSPACE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[
    PricingQuoteWorkspaceDetailEffectiveCriticalityType1
] = {
    "high",
    "low",
    "medium",
}


def check_pricing_quote_workspace_detail_effective_criticality_type_1(
    value: str,
) -> PricingQuoteWorkspaceDetailEffectiveCriticalityType1:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
