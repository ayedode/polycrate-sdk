from typing import Literal

ApiV1PricingQuoteWorkspacesListStateErrorComponentAttr = Literal["state"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesListStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_pricing_quote_workspaces_list_state_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListStateErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
