from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_pricing_calculator_states_formalize_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
