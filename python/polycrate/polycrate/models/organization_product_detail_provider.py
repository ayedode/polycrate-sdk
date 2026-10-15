from typing import Literal

OrganizationProductDetailProvider = Literal[
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

ORGANIZATION_PRODUCT_DETAIL_PROVIDER_VALUES: set[OrganizationProductDetailProvider] = {
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


def check_organization_product_detail_provider(value: str) -> OrganizationProductDetailProvider:
    if value in ORGANIZATION_PRODUCT_DETAIL_PROVIDER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_PRODUCT_DETAIL_PROVIDER_VALUES!r}")
