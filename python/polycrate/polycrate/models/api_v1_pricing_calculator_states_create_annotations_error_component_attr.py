from typing import Literal

ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_calculator_states_create_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
