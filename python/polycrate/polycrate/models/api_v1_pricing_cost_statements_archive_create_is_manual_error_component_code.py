from typing import Literal

ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_archive_create_is_manual_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
