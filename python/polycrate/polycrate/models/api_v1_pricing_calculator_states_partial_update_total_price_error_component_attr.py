from typing import Literal

ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponentAttr = Literal["total_price"]

API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponentAttr
] = {
    "total_price",
}


def check_api_v1_pricing_calculator_states_partial_update_total_price_error_component_attr(
    value: str,
) -> ApiV1PricingCalculatorStatesPartialUpdateTotalPriceErrorComponentAttr:
    if value in API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_PARTIAL_UPDATE_TOTAL_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
