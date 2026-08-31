from typing import Literal

ApiV1PricingQuoteWorkspacesListScopeErrorComponentAttr = Literal["scope"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesListScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_pricing_quote_workspaces_list_scope_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListScopeErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
