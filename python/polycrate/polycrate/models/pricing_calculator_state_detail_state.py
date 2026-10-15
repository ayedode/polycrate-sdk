from typing import Literal

PricingCalculatorStateDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_CALCULATOR_STATE_DETAIL_STATE_VALUES: set[PricingCalculatorStateDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_calculator_state_detail_state(value: str) -> PricingCalculatorStateDetailState:
    if value in PRICING_CALCULATOR_STATE_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_STATE_VALUES!r}")
