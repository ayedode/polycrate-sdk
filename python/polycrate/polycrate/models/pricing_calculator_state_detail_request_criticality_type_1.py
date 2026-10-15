from typing import Literal

PricingCalculatorStateDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PricingCalculatorStateDetailRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_pricing_calculator_state_detail_request_criticality_type_1(
    value: str,
) -> PricingCalculatorStateDetailRequestCriticalityType1:
    if value in PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
