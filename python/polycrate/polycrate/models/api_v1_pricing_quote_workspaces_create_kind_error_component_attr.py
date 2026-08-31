from typing import Literal

ApiV1PricingQuoteWorkspacesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_quote_workspaces_create_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
