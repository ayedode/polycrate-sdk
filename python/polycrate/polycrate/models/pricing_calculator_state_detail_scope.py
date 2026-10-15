from typing import Literal

PricingCalculatorStateDetailScope = Literal["system", "user"]

PRICING_CALCULATOR_STATE_DETAIL_SCOPE_VALUES: set[PricingCalculatorStateDetailScope] = {
    "system",
    "user",
}


def check_pricing_calculator_state_detail_scope(value: str) -> PricingCalculatorStateDetailScope:
    if value in PRICING_CALCULATOR_STATE_DETAIL_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_SCOPE_VALUES!r}")
