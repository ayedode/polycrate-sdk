from typing import Literal

ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_LAST_ACCESS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_pricing_calculator_states_update_last_access_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_LAST_ACCESS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_LAST_ACCESS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
