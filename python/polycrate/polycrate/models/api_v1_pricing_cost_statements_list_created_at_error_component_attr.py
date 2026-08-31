from typing import Literal

ApiV1PricingCostStatementsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_pricing_cost_statements_list_created_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsListCreatedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
