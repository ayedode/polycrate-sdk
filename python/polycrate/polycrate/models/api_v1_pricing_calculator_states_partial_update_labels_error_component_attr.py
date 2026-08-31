from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_pricing_calculator_states_partial_update_labels_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateLabelsErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
