from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponentCode = Literal["invalid", "null"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_pricing_quote_workspaces_update_debug_mode_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
