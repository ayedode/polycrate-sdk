from typing import Literal

ApiV1PricingCalculatorStatesCreateBookingIdErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_PRICING_CALCULATOR_STATES_CREATE_BOOKING_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesCreateBookingIdErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pricing_calculator_states_create_booking_id_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateBookingIdErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_BOOKING_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_BOOKING_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
