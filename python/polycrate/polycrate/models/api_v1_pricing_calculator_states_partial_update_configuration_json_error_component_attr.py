from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponentAttr = Literal["configuration_json"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponentAttr
] = {
    "configuration_json",
}


def check_api_v1_pricing_calculator_states_partial_update_configuration_json_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateConfigurationJsonErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
