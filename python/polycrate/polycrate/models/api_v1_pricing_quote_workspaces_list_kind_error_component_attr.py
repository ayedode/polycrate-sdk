from typing import Literal

ApiV1PricingQuoteWorkspacesListKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTE_WORKSPACES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_quote_workspaces_list_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesListKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
