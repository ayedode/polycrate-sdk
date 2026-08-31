from typing import Literal

ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pricing_quote_workspaces_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
