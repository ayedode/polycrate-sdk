from typing import Literal

PatchedPricingRuleDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedPricingRuleDetailRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pricing_rule_detail_request_criticality_type_1(
    value: str,
) -> PatchedPricingRuleDetailRequestCriticalityType1:
    if value in PATCHED_PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
