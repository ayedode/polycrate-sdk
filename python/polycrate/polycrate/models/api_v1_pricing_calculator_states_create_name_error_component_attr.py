from typing import Literal

ApiV1PricingCalculatorStatesCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_calculator_states_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
