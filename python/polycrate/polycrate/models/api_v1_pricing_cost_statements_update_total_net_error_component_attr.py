from typing import Literal

ApiV1PricingCostStatementsUpdateTotalNetErrorComponentAttr = Literal["total_net"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_TOTAL_NET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateTotalNetErrorComponentAttr
] = {
    "total_net",
}


def check_api_v1_pricing_cost_statements_update_total_net_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateTotalNetErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_TOTAL_NET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_TOTAL_NET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
