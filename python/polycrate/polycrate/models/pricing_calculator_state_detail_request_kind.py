from typing import Literal

PricingCalculatorStateDetailRequestKind = Literal["generic"]

PRICING_CALCULATOR_STATE_DETAIL_REQUEST_KIND_VALUES: set[PricingCalculatorStateDetailRequestKind] = {
    "generic",
}


def check_pricing_calculator_state_detail_request_kind(value: str) -> PricingCalculatorStateDetailRequestKind:
    if value in PRICING_CALCULATOR_STATE_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_REQUEST_KIND_VALUES!r}"
    )
