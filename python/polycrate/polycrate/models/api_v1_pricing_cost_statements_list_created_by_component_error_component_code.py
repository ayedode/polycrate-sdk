from typing import Literal

ApiV1PricingCostStatementsListCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsListCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_cost_statements_list_created_by_component_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsListCreatedByComponentErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
