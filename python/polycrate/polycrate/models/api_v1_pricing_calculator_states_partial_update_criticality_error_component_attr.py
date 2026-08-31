from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_pricing_calculator_states_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
