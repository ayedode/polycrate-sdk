from typing import Literal

ApiV1PricingCalculatorStatesListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_CALCULATOR_STATES_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1PricingCalculatorStatesListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_calculator_states_list_created_by_component(
    value: str,
) -> ApiV1PricingCalculatorStatesListCreatedByComponent:
    if value in API_V1_PRICING_CALCULATOR_STATES_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_CALCULATOR_STATES_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
