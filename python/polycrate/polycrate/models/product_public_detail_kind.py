from typing import Literal

ProductPublicDetailKind = Literal[
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

PRODUCT_PUBLIC_DETAIL_KIND_VALUES: set[ProductPublicDetailKind] = {
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


def check_product_public_detail_kind(value: str) -> ProductPublicDetailKind:
    if value in PRODUCT_PUBLIC_DETAIL_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_DETAIL_KIND_VALUES!r}")
