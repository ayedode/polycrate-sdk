from typing import Literal

ApiV1PricingCostStatementsListCreatedByComponent = Literal["api", "cli", "operator"]

API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_BY_COMPONENT_VALUES: set[
    ApiV1PricingCostStatementsListCreatedByComponent
] = {
    "api",
    "cli",
    "operator",
}


def check_api_v1_pricing_cost_statements_list_created_by_component(
    value: str,
) -> ApiV1PricingCostStatementsListCreatedByComponent:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_BY_COMPONENT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_BY_COMPONENT_VALUES!r}"
    )
