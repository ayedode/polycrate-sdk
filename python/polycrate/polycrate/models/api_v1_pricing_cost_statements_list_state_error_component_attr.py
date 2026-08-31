from typing import Literal

ApiV1PricingCostStatementsListStateErrorComponentAttr = Literal["state"]

API_V1_PRICING_COST_STATEMENTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_pricing_cost_statements_list_state_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsListStateErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
