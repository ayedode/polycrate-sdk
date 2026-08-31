from typing import Literal

ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_cost_statements_void_create_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsVoidCreateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_VOID_CREATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
