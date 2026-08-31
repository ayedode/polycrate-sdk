from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponentAttr = Literal["booking_id"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_BOOKING_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponentAttr
] = {
    "booking_id",
}


def check_api_v1_pricing_calculator_states_partial_update_booking_id_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateBookingIdErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_BOOKING_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_BOOKING_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
