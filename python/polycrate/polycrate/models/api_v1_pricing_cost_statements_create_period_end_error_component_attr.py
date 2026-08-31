from typing import Literal

ApiV1PricingCostStatementsCreatePeriodEndErrorComponentAttr = Literal["period_end"]

API_V1_PRICING_COST_STATEMENTS_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsCreatePeriodEndErrorComponentAttr
] = {
    "period_end",
}


def check_api_v1_pricing_cost_statements_create_period_end_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsCreatePeriodEndErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
