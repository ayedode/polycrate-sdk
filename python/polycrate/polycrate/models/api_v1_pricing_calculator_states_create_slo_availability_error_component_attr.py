from typing import Literal

ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_pricing_calculator_states_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
