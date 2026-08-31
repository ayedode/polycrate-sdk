from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_pricing_calculator_states_formalize_create_display_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateDisplayNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
