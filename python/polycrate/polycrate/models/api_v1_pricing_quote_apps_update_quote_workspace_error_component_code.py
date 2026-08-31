from typing import Literal

ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "null", "required"
]

API_V1_PRICING_QUOTE_APPS_UPDATE_QUOTE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_pricing_quote_apps_update_quote_workspace_error_component_code(
    value: str,
) -> ApiV1PricingQuoteAppsUpdateQuoteWorkspaceErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_APPS_UPDATE_QUOTE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_APPS_UPDATE_QUOTE_WORKSPACE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
