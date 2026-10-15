from typing import Literal

PricingRuleDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PRICING_RULE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PricingRuleDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_rule_detail_criticality_type_3_type_1(value: str) -> PricingRuleDetailCriticalityType3Type1:
    if value in PRICING_RULE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
