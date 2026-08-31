from typing import Literal

ApiV1PricingCalculatorStatesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_CALCULATOR_STATES_LIST_STATE_VALUES: set[ApiV1PricingCalculatorStatesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_calculator_states_list_state(value: str) -> ApiV1PricingCalculatorStatesListState:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_STATE_VALUES!r}"
    )
