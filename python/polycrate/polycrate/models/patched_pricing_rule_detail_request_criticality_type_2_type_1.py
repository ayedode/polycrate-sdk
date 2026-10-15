from typing import Literal

PatchedPricingRuleDetailRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedPricingRuleDetailRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pricing_rule_detail_request_criticality_type_2_type_1(
    value: str,
) -> PatchedPricingRuleDetailRequestCriticalityType2Type1:
    if value in PATCHED_PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_RULE_DETAIL_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
