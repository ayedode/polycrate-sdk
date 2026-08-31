from typing import Literal

ApiV1PricingCostStatementsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pricing_cost_statements_list_created_at_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsListCreatedAtErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
