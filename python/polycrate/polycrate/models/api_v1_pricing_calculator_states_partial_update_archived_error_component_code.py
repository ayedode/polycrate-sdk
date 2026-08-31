from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
