from typing import Literal

PricingCalculatorStateDetailCriticalityType1 = Literal["", "high", "low", "medium"]

PRICING_CALCULATOR_STATE_DETAIL_CRITICALITY_TYPE_1_VALUES: set[PricingCalculatorStateDetailCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_calculator_state_detail_criticality_type_1(
    value: str,
) -> PricingCalculatorStateDetailCriticalityType1:
    if value in PRICING_CALCULATOR_STATE_DETAIL_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_CRITICALITY_TYPE_1_VALUES!r}"
    )
