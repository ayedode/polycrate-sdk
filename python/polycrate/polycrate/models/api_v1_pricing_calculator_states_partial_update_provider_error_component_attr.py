from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pricing_calculator_states_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
