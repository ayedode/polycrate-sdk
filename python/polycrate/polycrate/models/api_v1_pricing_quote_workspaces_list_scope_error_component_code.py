from typing import Literal

ApiV1PricingQuoteWorkspacesListScopeErrorComponentCode = Literal["invalid_choice"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PricingQuoteWorkspacesListScopeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_pricing_quote_workspaces_list_scope_error_component_code(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListScopeErrorComponentCode:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
