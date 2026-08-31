from typing import Literal

ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_pricing_calculator_states_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
