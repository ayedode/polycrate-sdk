from typing import Literal

ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_pricing_calculator_states_update_annotations_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
