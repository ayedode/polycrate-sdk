from typing import Literal

ApiV1PricingQuoteWorkspacesListKind = Literal["generic"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_KIND_VALUES: set[ApiV1PricingQuoteWorkspacesListKind] = {
    "generic",
}


def check_api_v1_pricing_quote_workspaces_list_kind(value: str) -> ApiV1PricingQuoteWorkspacesListKind:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_KIND_VALUES!r}")
