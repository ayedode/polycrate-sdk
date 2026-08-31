from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_pricing_calculator_states_formalize_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateTolerationsErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
