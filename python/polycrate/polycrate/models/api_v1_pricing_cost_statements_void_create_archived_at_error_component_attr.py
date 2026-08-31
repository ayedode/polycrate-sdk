from typing import Literal

ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_cost_statements_void_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
