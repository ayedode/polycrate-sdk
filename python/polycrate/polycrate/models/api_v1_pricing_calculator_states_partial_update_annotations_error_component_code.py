from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_calculator_states_partial_update_annotations_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
