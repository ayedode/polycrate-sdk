from typing import Literal

ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_update_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
