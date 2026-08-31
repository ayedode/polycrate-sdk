from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_pricing_calculator_states_formalize_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
