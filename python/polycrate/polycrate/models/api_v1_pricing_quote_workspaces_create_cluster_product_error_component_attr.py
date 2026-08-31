from typing import Literal

ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponentAttr = Literal["cluster_product"]

API_V1_PRICING_QUOTE_WORKSPACES_CREATE_CLUSTER_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponentAttr
] = {
    "cluster_product",
}


def check_api_v1_pricing_quote_workspaces_create_cluster_product_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_CREATE_CLUSTER_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_CREATE_CLUSTER_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
