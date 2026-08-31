from typing import Literal

ApiV1PricingCostStatementsVoidCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pricing_cost_statements_void_create_kind_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateKindErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
