from typing import Literal

ApiV1PricingCostStatementsListKindErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_COST_STATEMENTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsListKindErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_cost_statements_list_kind_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsListKindErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
