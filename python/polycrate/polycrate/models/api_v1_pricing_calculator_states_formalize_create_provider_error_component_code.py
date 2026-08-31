from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_calculator_states_formalize_create_provider_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
