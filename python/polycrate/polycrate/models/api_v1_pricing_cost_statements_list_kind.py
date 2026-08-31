from typing import Literal

ApiV1PricingCostStatementsListKind = Literal["generic"]

API_V1_PRICING_COST_STATEMENTS_LIST_KIND_VALUES: set[ApiV1PricingCostStatementsListKind] = {
    "generic",
}


def check_api_v1_pricing_cost_statements_list_kind(value: str) -> ApiV1PricingCostStatementsListKind:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_KIND_VALUES!r}")
