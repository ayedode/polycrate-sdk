from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponentAttr = Literal["cluster_quoted_price"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_CLUSTER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponentAttr
] = {
    "cluster_quoted_price",
}


def check_api_v1_pricing_quote_workspaces_archive_create_cluster_quoted_price_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateClusterQuotedPriceErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_CLUSTER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_CLUSTER_QUOTED_PRICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
