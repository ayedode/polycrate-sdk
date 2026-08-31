from typing import Literal

ApiV1PricingCalculatorStatesListKind = Literal["generic"]

API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_VALUES: set[ApiV1PricingCalculatorStatesListKind] = {
    "generic",
}


def check_api_v1_pricing_calculator_states_list_kind(value: str) -> ApiV1PricingCalculatorStatesListKind:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_VALUES!r}"
    )
