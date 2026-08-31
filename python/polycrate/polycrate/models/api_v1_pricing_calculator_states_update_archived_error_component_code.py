from typing import Literal

ApiV1PricingCalculatorStatesUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_update_archived_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateArchivedErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
