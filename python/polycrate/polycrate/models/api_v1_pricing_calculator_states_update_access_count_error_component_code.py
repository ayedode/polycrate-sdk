from typing import Literal

ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_ACCESS_COUNT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_pricing_calculator_states_update_access_count_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_ACCESS_COUNT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_ACCESS_COUNT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
