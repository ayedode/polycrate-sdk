from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_pricing_calculator_states_partial_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
