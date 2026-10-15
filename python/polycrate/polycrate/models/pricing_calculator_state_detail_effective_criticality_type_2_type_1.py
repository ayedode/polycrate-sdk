from typing import Literal

PricingCalculatorStateDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PRICING_CALCULATOR_STATE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PricingCalculatorStateDetailEffectiveCriticalityType2Type1
] = {
    "high",
    "low",
    "medium",
}


def check_pricing_calculator_state_detail_effective_criticality_type_2_type_1(
    value: str,
) -> PricingCalculatorStateDetailEffectiveCriticalityType2Type1:
    if value in PRICING_CALCULATOR_STATE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
