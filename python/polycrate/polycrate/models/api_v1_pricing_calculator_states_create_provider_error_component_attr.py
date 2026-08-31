from typing import Literal

ApiV1PricingCalculatorStatesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_calculator_states_create_provider_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateProviderErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
