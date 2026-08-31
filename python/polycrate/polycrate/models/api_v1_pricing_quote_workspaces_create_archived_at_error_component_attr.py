from typing import Literal

ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_pricing_quote_workspaces_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
