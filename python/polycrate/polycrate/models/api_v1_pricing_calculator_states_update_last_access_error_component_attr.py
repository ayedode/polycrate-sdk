from typing import Literal

ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponentAttr = Literal["last_access"]

API_V1_PRICING_CALCULATOR_STATES_UPDATE_LAST_ACCESS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponentAttr
] = {
    "last_access",
}


def check_api_v1_pricing_calculator_states_update_last_access_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesUpdateLastAccessErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_UPDATE_LAST_ACCESS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_UPDATE_LAST_ACCESS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
