from typing import Literal

ApiV1PricingCalculatorStatesListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_PRICING_CALCULATOR_STATES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_pricing_calculator_states_list_created_at_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesListCreatedAtErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
