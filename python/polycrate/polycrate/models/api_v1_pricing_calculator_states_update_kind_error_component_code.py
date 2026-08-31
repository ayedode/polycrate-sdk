from typing import Literal

ApiV1PricingCalculatorStatesUpdateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_calculator_states_update_kind_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateKindErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
