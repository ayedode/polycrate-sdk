from typing import Literal

ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponentCode = Literal["invalid"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_calculator_states_update_configuration_json_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_CODE_VALUES!r}"
    )
