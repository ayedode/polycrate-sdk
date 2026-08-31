from typing import Literal

ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponentAttr = Literal["quote_workspace"]

API_V1_PRICING_QUOTE_APPS_UPDATE_QUOTE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponentAttr
] = {
    "quote_workspace",
}


def check_api_v1_pricing_quote_apps_update_quote_workspace_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_QUOTE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_QUOTE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
