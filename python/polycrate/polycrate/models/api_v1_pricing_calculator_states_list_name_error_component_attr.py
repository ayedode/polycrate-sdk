from typing import Literal

ApiV1PricingCalculatorStatesListNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_CALCULATOR_STATES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesListNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_calculator_states_list_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesListNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
