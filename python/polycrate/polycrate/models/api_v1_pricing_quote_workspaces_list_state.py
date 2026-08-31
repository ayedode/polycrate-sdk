from typing import Literal

ApiV1PricingQuoteWorkspacesListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_STATE_VALUES: set[ApiV1PricingQuoteWorkspacesListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_pricing_quote_workspaces_list_state(value: str) -> ApiV1PricingQuoteWorkspacesListState:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_STATE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_STATE_VALUES!r}"
    )
