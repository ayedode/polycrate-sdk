from typing import Literal

ApiV1PricingCostStatementsCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_cost_statements_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
