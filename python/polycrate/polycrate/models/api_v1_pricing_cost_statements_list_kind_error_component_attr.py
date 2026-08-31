from typing import Literal

ApiV1PricingCostStatementsListKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_COST_STATEMENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_cost_statements_list_kind_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsListKindErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
