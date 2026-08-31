from typing import Literal

ApiV1PricingProductsListKind = Literal[
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

API_V1_PRICING_PRODUCTS_LIST_KIND_VALUES: set[ApiV1PricingProductsListKind] = {
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


def check_api_v1_pricing_products_list_kind(value: str) -> ApiV1PricingProductsListKind:
    if value in API_V1_PRICING_PRODUCTS_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PRICING_PRODUCTS_LIST_KIND_VALUES!r}")
