from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponentAttr = Literal["debug_mode"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponentAttr
] = {
    "debug_mode",
}


def check_api_v1_pricing_quote_workspaces_update_debug_mode_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateDebugModeErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_DEBUG_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
