from typing import Literal

ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponentAttr
] = {
    "created_at",
}


def check_api_v1_pricing_quote_workspaces_list_created_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListCreatedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
