from typing import Literal

PricingCalculatorStateDetailKind = Literal["generic"]

PRICING_CALCULATOR_STATE_DETAIL_KIND_VALUES: set[PricingCalculatorStateDetailKind] = {
    "generic",
}


def check_pricing_calculator_state_detail_kind(value: str) -> PricingCalculatorStateDetailKind:
    if value in PRICING_CALCULATOR_STATE_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_KIND_VALUES!r}")
