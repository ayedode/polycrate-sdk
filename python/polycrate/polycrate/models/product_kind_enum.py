from typing import Literal

ProductKindEnum = Literal[
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

PRODUCT_KIND_ENUM_VALUES: set[ProductKindEnum] = {
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


def check_product_kind_enum(value: str) -> ProductKindEnum:
    if value in PRODUCT_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRODUCT_KIND_ENUM_VALUES!r}")
