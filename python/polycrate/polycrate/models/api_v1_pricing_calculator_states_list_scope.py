from typing import Literal

ApiV1PricingCalculatorStatesListScope = Literal["system", "user"]

API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_VALUES: set[ApiV1PricingCalculatorStatesListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_calculator_states_list_scope(value: str) -> ApiV1PricingCalculatorStatesListScope:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_VALUES!r}"
    )
