from typing import Literal

ApiV1PricingCalculatorStatesUpdateLabelsErrorComponentCode = Literal["invalid"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_calculator_states_update_labels_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateLabelsErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
