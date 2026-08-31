from typing import Literal

ApiV1PricingCalculatorStatesListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_calculator_states_list_kind_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesListKindErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
