from typing import Literal

ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
