from typing import Literal

ApiV1PricingCalculatorStatesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_PRICING_CALCULATOR_STATES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_pricing_calculator_states_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesListUpdatedAtErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
