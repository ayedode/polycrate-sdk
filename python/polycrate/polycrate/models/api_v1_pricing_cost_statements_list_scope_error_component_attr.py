from typing import Literal

ApiV1PricingCostStatementsListScopeErrorComponentAttr = Literal["scope"]

API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_pricing_cost_statements_list_scope_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsListScopeErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
