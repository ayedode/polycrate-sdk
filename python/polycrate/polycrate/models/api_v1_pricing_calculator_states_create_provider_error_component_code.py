from typing import Literal

ApiV1PricingCalculatorStatesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCalculatorStatesCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_calculator_states_create_provider_error_component_code(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateProviderErrorComponentCode:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
