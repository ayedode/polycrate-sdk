from typing import Literal

PricingRuleDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PRICING_RULE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[PricingRuleDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_pricing_rule_detail_effective_criticality_type_1(value: str) -> PricingRuleDetailEffectiveCriticalityType1:
    if value in PRICING_RULE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_RULE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
