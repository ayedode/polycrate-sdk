from typing import Literal

ApiV1PricingCostStatementsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_COST_STATEMENTS_LIST_STATE_VALUES: set[ApiV1PricingCostStatementsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_cost_statements_list_state(value: str) -> ApiV1PricingCostStatementsListState:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_STATE_VALUES!r}")
