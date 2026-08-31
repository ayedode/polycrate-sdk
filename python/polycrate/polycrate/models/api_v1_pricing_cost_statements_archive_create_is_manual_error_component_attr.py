from typing import Literal

ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponentAttr = Literal["is_manual"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponentAttr
] = {
    "is_manual",
}


def check_api_v1_pricing_cost_statements_archive_create_is_manual_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_IS_MANUAL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
