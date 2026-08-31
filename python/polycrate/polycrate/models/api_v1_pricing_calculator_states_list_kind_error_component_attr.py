from typing import Literal

ApiV1PricingCalculatorStatesListKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_calculator_states_list_kind_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesListKindErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
