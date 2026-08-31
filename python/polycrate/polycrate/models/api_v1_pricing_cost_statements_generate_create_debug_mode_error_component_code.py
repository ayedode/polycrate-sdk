from typing import Literal

ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_cost_statements_generate_create_debug_mode_error_component_code(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponentCode:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
