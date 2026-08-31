from typing import Literal

ApiV1PricingOrganizationProductsListProductKind = Literal[
    "assistant",
    "block-storage",
    "dnszone",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "support",
]

API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_KIND_VALUES: set[ApiV1PricingOrganizationProductsListProductKind] = {
    "assistant",
    "block-storage",
    "dnszone",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "support",
}


def check_api_v1_pricing_organization_products_list_product_kind(
    value: str,
) -> ApiV1PricingOrganizationProductsListProductKind:
    if value in API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_ORGANIZATION_PRODUCTS_LIST_PRODUCT_KIND_VALUES!r}"
    )
