from typing import Literal

ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_quote_workspaces_create_archived_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
