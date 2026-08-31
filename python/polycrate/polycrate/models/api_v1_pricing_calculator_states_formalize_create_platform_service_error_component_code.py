from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_calculator_states_formalize_create_platform_service_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreatePlatformServiceErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
