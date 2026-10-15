from typing import Literal

ProductPublicListKind = Literal[
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

PRODUCT_PUBLIC_LIST_KIND_VALUES: set[ProductPublicListKind] = {
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


def check_product_public_list_kind(value: str) -> ProductPublicListKind:
    if value in PRODUCT_PUBLIC_LIST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_PUBLIC_LIST_KIND_VALUES!r}")
