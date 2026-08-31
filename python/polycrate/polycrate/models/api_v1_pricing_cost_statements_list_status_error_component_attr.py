from typing import Literal

ApiV1PricingCostStatementsListStatusErrorComponentAttr = Literal["status"]

API_V1_PRICING_COST_STATEMENTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsListStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_pricing_cost_statements_list_status_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsListStatusErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
