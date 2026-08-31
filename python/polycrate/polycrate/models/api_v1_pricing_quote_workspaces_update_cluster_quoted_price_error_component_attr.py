from typing import Literal

ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponentAttr = Literal["cluster_quoted_price"]

API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CLUSTER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponentAttr
] = {
    "cluster_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_update_cluster_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesUpdateClusterQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CLUSTER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_UPDATE_CLUSTER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
