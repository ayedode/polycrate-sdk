from typing import Literal

ProductDetailRequestKind = Literal[
    "assistant",
    "block-storage",
    "dnszone",
    "domain",
    "endpoint-monitor",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "registry-storage",
    "secrets-namespace",
    "support",
]

PRODUCT_DETAIL_REQUEST_KIND_VALUES: set[ProductDetailRequestKind] = {
    "assistant",
    "block-storage",
    "dnszone",
    "domain",
    "endpoint-monitor",
    "host",
    "k8sapp",
    "k8scluster",
    "loadbalancer",
    "object-storage",
    "project",
    "registry-storage",
    "secrets-namespace",
    "support",
}


def check_product_detail_request_kind(value: str) -> ProductDetailRequestKind:
    if value in PRODUCT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_DETAIL_REQUEST_KIND_VALUES!r}")
