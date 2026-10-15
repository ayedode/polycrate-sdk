from typing import Literal

PricingQuoteWorkspaceDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PRICING_QUOTE_WORKSPACE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PricingQuoteWorkspaceDetailCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_quote_workspace_detail_criticality_type_3_type_1(
    value: str,
) -> PricingQuoteWorkspaceDetailCriticalityType3Type1:
    if value in PRICING_QUOTE_WORKSPACE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_QUOTE_WORKSPACE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
