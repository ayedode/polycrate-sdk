from typing import Literal

PatchedProductDetailRequestKind = Literal[
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

PATCHED_PRODUCT_DETAIL_REQUEST_KIND_VALUES: set[PatchedProductDetailRequestKind] = {
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


def check_patched_product_detail_request_kind(value: str) -> PatchedProductDetailRequestKind:
    if value in PATCHED_PRODUCT_DETAIL_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PRODUCT_DETAIL_REQUEST_KIND_VALUES!r}")
