from typing import Literal

PricingRuleListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

PRICING_RULE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PricingRuleListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_pricing_rule_list_effective_criticality_type_3_type_1(
    value: str,
) -> PricingRuleListEffectiveCriticalityType3Type1:
    if value in PRICING_RULE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_RULE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
