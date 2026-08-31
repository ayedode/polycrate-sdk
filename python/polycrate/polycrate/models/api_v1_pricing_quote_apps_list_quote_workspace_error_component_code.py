from typing import Literal

ApiV1PricingQuoteAppsListQuoteWorkspaceErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_PRICING_QUOTE_APPS_LIST_QUOTE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsListQuoteWorkspaceErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_pricing_quote_apps_list_quote_workspace_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsListQuoteWorkspaceErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_LIST_QUOTE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_LIST_QUOTE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
