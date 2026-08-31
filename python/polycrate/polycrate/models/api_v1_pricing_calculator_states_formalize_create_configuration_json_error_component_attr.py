from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponentAttr = Literal["configuration_json"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponentAttr
] = {
    "configuration_json",
}


def check_api_v1_pricing_calculator_states_formalize_create_configuration_json_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateConfigurationJsonErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_CONFIGURATION_JSON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
