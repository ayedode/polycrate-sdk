from typing import Literal

ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_pricing_calculator_states_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
