from typing import Literal

ProductSimpleKind = Literal[
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

PRODUCT_SIMPLE_KIND_VALUES: set[ProductSimpleKind] = {
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


def check_product_simple_kind(value: str) -> ProductSimpleKind:
    if value in PRODUCT_SIMPLE_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_SIMPLE_KIND_VALUES!r}")
