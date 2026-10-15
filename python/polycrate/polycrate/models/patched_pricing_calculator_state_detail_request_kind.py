from typing import Literal

PatchedPricingCalculatorStateDetailRequestKind = Literal["generic"]

PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_KIND_VALUES: set[PatchedPricingCalculatorStateDetailRequestKind] = {
    "generic",
}


def check_patched_pricing_calculator_state_detail_request_kind(
    value: str,
) -> PatchedPricingCalculatorStateDetailRequestKind:
    if value in PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PRICING_CALCULATOR_STATE_DETAIL_REQUEST_KIND_VALUES!r}"
    )
