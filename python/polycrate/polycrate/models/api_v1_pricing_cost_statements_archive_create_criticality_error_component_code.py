from typing import Literal

ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_cost_statements_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
