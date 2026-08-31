from typing import Literal

ApiV1PricingCalculatorStatesCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateDebugModeErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
