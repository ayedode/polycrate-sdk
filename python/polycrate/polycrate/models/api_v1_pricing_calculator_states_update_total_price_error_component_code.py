from typing import Literal

ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_pricing_calculator_states_update_total_price_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateTotalPriceErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
