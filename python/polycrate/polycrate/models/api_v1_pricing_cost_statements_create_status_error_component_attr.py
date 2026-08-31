from typing import Literal

ApiV1PricingCostStatementsCreateStatusErrorComponentAttr = Literal["status"]

API_V1_PRICING_COST_STATEMENTS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_pricing_cost_statements_create_status_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreateStatusErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
