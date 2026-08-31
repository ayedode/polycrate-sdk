from typing import Literal

ApiV1PricingCostStatementsUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_pricing_cost_statements_update_status_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateStatusErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
