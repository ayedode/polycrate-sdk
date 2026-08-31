from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_calculator_states_formalize_create_annotations_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateAnnotationsErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
