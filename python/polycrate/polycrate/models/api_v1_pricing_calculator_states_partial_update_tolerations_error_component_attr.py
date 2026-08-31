from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_calculator_states_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
