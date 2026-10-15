from typing import Literal

PatchedProductDetailRequestProvider = Literal[
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
]

PATCHED_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedProductDetailRequestProvider] = {
    "bare_metal",
    "cloudflare",
    "generic",
    "helm",
    "hetzner_cloud",
    "hetzner_robot",
    "kubernetes",
    "loopback",
    "polycrate",
    "powerdns",
    "rook-ceph",
    "system",
    "victorialogs",
}


def check_patched_product_detail_request_provider(value: str) -> PatchedProductDetailRequestProvider:
    if value in PATCHED_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES!r}")
