from typing import Literal

ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_calculator_states_update_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
