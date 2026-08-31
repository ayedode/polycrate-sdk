from typing import Literal

ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_calculator_states_archive_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesArchiveCreateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_ARCHIVE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
