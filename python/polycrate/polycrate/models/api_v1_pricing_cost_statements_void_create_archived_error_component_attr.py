from typing import Literal

ApiV1PricingCostStatementsVoidCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_cost_statements_void_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
