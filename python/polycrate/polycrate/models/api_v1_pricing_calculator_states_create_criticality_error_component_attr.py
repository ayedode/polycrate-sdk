from typing import Literal

ApiV1PricingCalculatorStatesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_calculator_states_create_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
