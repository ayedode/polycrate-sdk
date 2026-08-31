from typing import Literal

ApiV1PricingCostStatementsVoidCreateIsManualErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateIsManualErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_void_create_is_manual_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateIsManualErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_IS_MANUAL_ERROR_COMPONENT_CODE_VALUES!r}"
    )
