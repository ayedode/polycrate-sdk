from typing import Literal

ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_cost_statements_generate_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsGenerateCreateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_GENERATE_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
