from typing import Literal

ApiV1PricingCalculatorStatesListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_calculator_states_list_scope_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesListScopeErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
