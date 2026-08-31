from typing import Literal

ApiV1PricingCostStatementsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_create_archived_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsCreateArchivedErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
