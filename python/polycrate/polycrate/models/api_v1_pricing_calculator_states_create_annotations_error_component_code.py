from typing import Literal

ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_calculator_states_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
