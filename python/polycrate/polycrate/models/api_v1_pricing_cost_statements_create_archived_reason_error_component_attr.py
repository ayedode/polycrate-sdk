from typing import Literal

ApiV1PricingCostStatementsCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_pricing_cost_statements_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
