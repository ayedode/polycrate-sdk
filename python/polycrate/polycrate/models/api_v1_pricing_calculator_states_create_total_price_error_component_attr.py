from typing import Literal

ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_CALCULATOR_STATES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_calculator_states_create_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesCreateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_CREATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
