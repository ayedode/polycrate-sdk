from typing import Literal

ApiV1PricingCalculatorStatesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_calculator_states_create_criticality_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
