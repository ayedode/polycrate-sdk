from typing import Literal

ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponentAttr = Literal["access_count"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponentAttr
] = {
    "access_count",
}


def check_api_v1_pricing_calculator_states_update_access_count_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateAccessCountErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
