from typing import Literal

ApiV1PricingCostStatementsListNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_PRICING_COST_STATEMENTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsListNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_pricing_cost_statements_list_name_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsListNameErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
