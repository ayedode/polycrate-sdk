from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponentAttr = Literal["name"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_pricing_calculator_states_formalize_create_name_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateNameErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
