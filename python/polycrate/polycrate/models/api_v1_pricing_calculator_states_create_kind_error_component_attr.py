from typing import Literal

ApiV1PricingCalculatorStatesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_calculator_states_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
