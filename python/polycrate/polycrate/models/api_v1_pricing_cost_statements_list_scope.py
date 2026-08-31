from typing import Literal

ApiV1PricingCostStatementsListScope = Literal["system", "user"]

API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_VALUES: set[ApiV1PricingCostStatementsListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_cost_statements_list_scope(value: str) -> ApiV1PricingCostStatementsListScope:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_VALUES!r}")
