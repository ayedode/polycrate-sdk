from typing import Literal

ApiV1PricingCostStatementsVoidCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_void_create_archived_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateArchivedErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
