from typing import Literal

ApiV1PricingQuoteWorkspacesListScope = Literal["system", "user"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_VALUES: set[ApiV1PricingQuoteWorkspacesListScope] = {
    "system",
    "user",
}


def check_api_v1_pricing_quote_workspaces_list_scope(value: str) -> ApiV1PricingQuoteWorkspacesListScope:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_SCOPE_VALUES!r}"
    )
