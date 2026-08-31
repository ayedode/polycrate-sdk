from typing import Literal

ApiV1PricingCostStatementsUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_COST_STATEMENTS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingCostStatementsUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_cost_statements_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingCostStatementsUpdateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_COST_STATEMENTS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_COST_STATEMENTS_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
