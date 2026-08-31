from typing import Literal

ApiV1PricingCostStatementsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_cost_statements_update_archived_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
