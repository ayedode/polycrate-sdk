from typing import Literal

ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponentAttr = Literal["loadbalancer_product"]

API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_PRODUCT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponentAttr
] = {
    "loadbalancer_product",
}


def check_api_v1_pricing_quote_workspaces_archive_create_loadbalancer_product_error_component_attr(
    value: str,
) -> ApiV1PricingQuoteWorkspacesArchiveCreateLoadbalancerProductErrorComponentAttr:
    if value in API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_PRODUCT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_QUOTE_WORKSPACES_ARCHIVE_CREATE_LOADBALANCER_PRODUCT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
