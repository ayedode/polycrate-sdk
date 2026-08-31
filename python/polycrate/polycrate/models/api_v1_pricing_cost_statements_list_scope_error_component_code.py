from typing import Literal

ApiV1PricingCostStatementsListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_cost_statements_list_scope_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsListScopeErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
