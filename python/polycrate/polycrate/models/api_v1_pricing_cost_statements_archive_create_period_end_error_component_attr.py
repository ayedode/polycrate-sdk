from typing import Literal

ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponentAttr = Literal["period_end"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponentAttr
] = {
    "period_end",
}


def check_api_v1_pricing_cost_statements_archive_create_period_end_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
