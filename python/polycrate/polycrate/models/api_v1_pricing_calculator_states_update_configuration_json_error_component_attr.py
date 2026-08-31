from typing import Literal

ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponentAttr = Literal["configuration_json"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponentAttr
] = {
    "configuration_json",
}


def check_api_v1_pricing_calculator_states_update_configuration_json_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateConfigurationJsonErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
