from typing import Literal

PricingQuoteWorkspaceListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

PRICING_QUOTE_WORKSPACE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PricingQuoteWorkspaceListEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_pricing_quote_workspace_list_effective_criticality_type_3_type_1(
    value: str,
) -> PricingQuoteWorkspaceListEffectiveCriticalityType3Type1:
    if value in PRICING_QUOTE_WORKSPACE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
