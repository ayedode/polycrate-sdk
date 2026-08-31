from typing import Literal

ApiV1PricingCalculatorStatesCreateAccessCountErrorComponentAttr = Literal["access_count"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateAccessCountErrorComponentAttr
] = {
    "access_count",
}


def check_api_v1_pricing_calculator_states_create_access_count_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateAccessCountErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
