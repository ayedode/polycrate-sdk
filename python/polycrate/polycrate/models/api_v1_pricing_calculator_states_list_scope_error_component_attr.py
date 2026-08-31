from typing import Literal

ApiV1PricingCalculatorStatesListScopeErrorComponentAttr = Literal["scope"]

API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_pricing_calculator_states_list_scope_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesListScopeErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
