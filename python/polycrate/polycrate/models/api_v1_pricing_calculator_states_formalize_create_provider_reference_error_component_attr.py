from typing import Literal

ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponentAttr = Literal["provider_reference"]

API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponentAttr
] = {
    "provider_reference",
}


def check_api_v1_pricing_calculator_states_formalize_create_provider_reference_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesFormalizeCreateProviderReferenceErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_FORMALIZE_CREATE_PROVIDER_REFERENCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
