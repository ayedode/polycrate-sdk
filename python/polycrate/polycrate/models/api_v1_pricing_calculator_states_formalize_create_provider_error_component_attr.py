from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_calculator_states_formalize_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
