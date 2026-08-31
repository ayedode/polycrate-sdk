from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_calculator_states_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
