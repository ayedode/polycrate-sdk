from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_pricing_quote_workspaces_update_kind_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateKindErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
