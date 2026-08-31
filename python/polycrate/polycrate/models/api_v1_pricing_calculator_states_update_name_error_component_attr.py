from typing import Literal

ApiV1PricingCalculatorStatesUpdateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_calculator_states_update_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
