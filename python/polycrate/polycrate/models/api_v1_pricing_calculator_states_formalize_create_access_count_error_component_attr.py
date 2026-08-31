from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponentAttr = Literal["access_count"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponentAttr
] = {
    "access_count",
}


def check_api_v1_pricing_calculator_states_formalize_create_access_count_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateAccessCountErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_ACCESS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
