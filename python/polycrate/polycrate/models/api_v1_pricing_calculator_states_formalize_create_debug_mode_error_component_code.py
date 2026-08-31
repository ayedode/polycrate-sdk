from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_formalize_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateDebugModeErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
