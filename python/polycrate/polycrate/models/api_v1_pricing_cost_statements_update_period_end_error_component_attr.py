from typing import Literal

ApiV1PricingCostStatementsUpdatePeriodEndErrorComponentAttr = Literal["period_end"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdatePeriodEndErrorComponentAttr
] = {
    "period_end",
}


def check_api_v1_pricing_cost_statements_update_period_end_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdatePeriodEndErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
