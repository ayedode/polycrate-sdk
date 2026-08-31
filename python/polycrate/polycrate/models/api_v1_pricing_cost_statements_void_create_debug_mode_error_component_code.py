from typing import Literal

ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_void_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
