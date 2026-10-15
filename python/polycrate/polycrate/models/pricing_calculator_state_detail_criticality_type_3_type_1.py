from typing import Literal

PricingCalculatorStateDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PRICING_CALCULATOR_STATE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PricingCalculatorStateDetailCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_calculator_state_detail_criticality_type_3_type_1(
    value: str,
) -> PricingCalculatorStateDetailCriticalityType3Type1:
    if value in PRICING_CALCULATOR_STATE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
