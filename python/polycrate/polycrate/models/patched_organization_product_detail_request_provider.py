from typing import Literal

PatchedOrganizationProductDetailRequestProvider = Literal[
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

PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES: set[PatchedOrganizationProductDetailRequestProvider] = {
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


def check_patched_organization_product_detail_request_provider(
    value: str,
) -> PatchedOrganizationProductDetailRequestProvider:
    if value in PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_PRODUCT_DETAIL_REQUEST_PROVIDER_VALUES!r}"
    )
