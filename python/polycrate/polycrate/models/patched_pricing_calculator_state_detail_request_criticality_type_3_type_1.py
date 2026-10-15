from typing import Literal

PatchedPricingCalculatorStateDetailRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedPricingCalculatorStateDetailRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_pricing_calculator_state_detail_request_criticality_type_3_type_1(
    value: str,
) -> PatchedPricingCalculatorStateDetailRequestCriticalityType3Type1:
    if value in PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
