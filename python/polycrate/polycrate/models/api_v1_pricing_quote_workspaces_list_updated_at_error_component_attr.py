from typing import Literal

ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponentAttr
] = {
    "updated_at",
}


def check_api_v1_pricing_quote_workspaces_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListUpdatedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
