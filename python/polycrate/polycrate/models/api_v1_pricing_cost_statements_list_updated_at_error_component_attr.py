from typing import Literal

ApiV1PricingCostStatementsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_PRICING_COST_STATEMENTS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_pricing_cost_statements_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsListUpdatedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
