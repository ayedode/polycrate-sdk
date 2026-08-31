from typing import Literal

ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_pricing_calculator_states_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateProviderIdErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
