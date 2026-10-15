from typing import Literal

PricingCalculatorStateListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PRICING_CALCULATOR_STATE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PricingCalculatorStateListEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_pricing_calculator_state_list_effective_criticality_type_2_type_1(
    value: str,
) -> PricingCalculatorStateListEffectiveCriticalityType2Type1:
    if value in PRICING_CALCULATOR_STATE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
