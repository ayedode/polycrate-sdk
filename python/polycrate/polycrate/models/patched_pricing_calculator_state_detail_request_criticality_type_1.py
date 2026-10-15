from typing import Literal

PatchedPricingCalculatorStateDetailRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES: set[
    PatchedPricingCalculatorStateDetailRequestCriticalityType1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pricing_calculator_state_detail_request_criticality_type_1(
    value: str,
) -> PatchedPricingCalculatorStateDetailRequestCriticalityType1:
    if value in PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
