from typing import Literal

ApiV1PricingCalculatorStatesListStateErrorComponentAttr = Literal["state"]

API_V1_PRICING_CALCULATOR_STATES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_pricing_calculator_states_list_state_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesListStateErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
