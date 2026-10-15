from typing import Literal

PricingCalculatorStateListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PRICING_CALCULATOR_STATE_LIST_STATE_VALUES: set[PricingCalculatorStateListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_pricing_calculator_state_list_state(value: str) -> PricingCalculatorStateListState:
    if value in PRICING_CALCULATOR_STATE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRICING_CALCULATOR_STATE_LIST_STATE_VALUES!r}")
