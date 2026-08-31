from typing import Literal

ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponentAttr = Literal["quote_workspace"]

API_V1_PRICING_QUOTE_APPS_CREATE_QUOTE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponentAttr
] = {
    "quote_workspace",
}


def check_api_v1_pricing_quote_apps_create_quote_workspace_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteAppsCreateQuoteWorkspaceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_APPS_CREATE_QUOTE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_CREATE_QUOTE_WORKSPACE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
