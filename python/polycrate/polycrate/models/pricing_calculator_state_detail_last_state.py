from typing import Literal

PricingCalculatorStateDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_CALCULATOR_STATE_DETAIL_LAST_STATE_VALUES: set[PricingCalculatorStateDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_calculator_state_detail_last_state(value: str) -> PricingCalculatorStateDetailLastState:
    if value in PRICING_CALCULATOR_STATE_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_DETAIL_LAST_STATE_VALUES!r}"
    )
