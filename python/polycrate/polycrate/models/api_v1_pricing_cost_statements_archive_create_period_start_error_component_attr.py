from typing import Literal

ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponentAttr = Literal["period_start"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PERIOD_START_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponentAttr
] = {
    "period_start",
}


def check_api_v1_pricing_cost_statements_archive_create_period_start_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PERIOD_START_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PERIOD_START_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
